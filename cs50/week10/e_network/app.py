import os

from cs50 import SQL
from datetime import datetime, timezone
from flask import Flask, redirect, render_template, request, session, jsonify, url_for
from flask_session import Session
from PIL import Image
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required

# Configure application
app = Flask(__name__)
app.debug = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Posts upload route
POSTS_PATH = 'static/posts'
# In Flask, a configuration variable is a named setting stored in your app’s configuration dictionary
# app.config that can be accessed anywhere.
app.config["POSTS_PATH"] = POSTS_PATH

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///fp.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Note: This program is vulnerable to race conditions, as sql queries are not wrapped in transactions.
@app.route("/")
@login_required
def feed():
    user_id = session["user_id"]
    # Select posts from db & sort by timestamp (for chronological feed)
    try:
        selected_user_ids = db.execute(
            "SELECT selected_user_id FROM filter WHERE user_id = ?",
            user_id
        )
        # Convert the list of dictionaries into a simple list of IDs
        selected_user_ids = [row['selected_user_id'] for row in selected_user_ids]
        # Ensure your own id is always selected
        selected_user_ids.append(user_id)

        posts = db.execute(
            """
            SELECT username, user_id, image_path, caption, timestamp FROM users
            JOIN posts ON users.id = posts.user_id
            WHERE posts.user_id IN (?)
            ORDER BY timestamp DESC
            """,
            selected_user_ids
        )
    except Exception:
        return "DB Error."
    return render_template("feed.html", posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    name = request.form.get("name")
    username = request.form.get("username")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")
    if not name:
        return "Must enter name."
    if not username:
        return "Must enter username."
    if len(name) > 25:
        return "Name too long."
    if len(username) > 20:
        return "Username too long."
    if not password:
        return "Must enter password."
    if not confirmation or \
    password != confirmation:
        return "Password & Confirmation do not match."
    username = username.lower()
    password = generate_password_hash(password)
    try:
        db.execute(
            "INSERT INTO users (name, username, hash) VALUES (?)",
            (name, username, password)
        )
        user_id = db.execute(
            "SELECT id FROM users WHERE username = ?",
            username
        )
        user_id=user_id[0]["id"]
        # If successfully registered, select all users for feed by default
        all_user_ids = db.execute(
            "SELECT id FROM users"
        )
        for user in all_user_ids:
            db.execute(
                "INSERT INTO filter (user_id, selected_user_id) VALUES (?, ?)",
                user_id,
                user["id"]
            )

        return render_template("success.html")

    # Since username is defined unique in db, trying to insert duplicate will throw Exception
    except Exception:
        return "Username already exists. Try another one."


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username")
    password = request.form.get("password")
    # Ensure username was submitted
    if not username:
        return "Must provide username."

    # Ensure password was submitted
    if not password:
        return "Must provide password."

    # Query database for username
    rows = db.execute("SELECT * FROM users WHERE username = ?", username)

    # Ensure username exists and password is correct
    if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
        return "Invalid username / password."

    # Remember which user has logged in
    session["user_id"] = rows[0]["id"]

    # Redirect user to home page
    return redirect(url_for("feed"))


@app.route("/posts", methods=["GET", "POST"])
@login_required
def posts():
    if request.method == "GET":
        return render_template("post.html")

    user_id = session["user_id"]
    img_input = request.files.get("img_upload")
    caption = request.form.get("caption")
    if not img_input:
        return "Must provide image."

    # Get image name from FileStorage object
    img_name = img_input.filename
    # Image validation
    try:
        # Image.open() tries to open img with Pillow library & raises exception
        # if file is not openable
        img = Image.open(img_input)
        query = db.execute("SELECT username, img_count FROM users WHERE id = :id", id=user_id)
        username = query[0]["username"]
        count = query[0]["img_count"]
    except Exception:
        return "Image format error."
    # Extension check
    exten = img_name.rsplit(".", 1) #exten is a list of all the splitted words, 1 parameter means 1 split only
    if len(exten) != 2:
        return "Invalid filename."
    exten[1] = exten[1].lower() #exten[0] is filename, exten[1] is extension
    extens = ["jpg", "jpeg", "png", "webp"]
    if exten[1] not in extens:
        return "Invalid image extension."
    # Rename image file to something safe
    img_name_safe = f"img_{username}_{count}.{exten[1]}"
    # Use os to create full path to image, compatible with all OS
    posts_path = os.path.join(app.config["POSTS_PATH"], img_name_safe)

    #    Image.open() reads the entire file & then moves the file's internal pointer to the end.
    #    .seek(0) method resets the pointer to the beginning of the file, allowing the subsequent
    #    .save() method to read the file's full content and save it correctly.
    img_input.seek(0)

    # Save the file using save(full_path) method from FileStorage object from request.files
    img_input.save(posts_path)
    # Insert info into db
    try:
        timestamp = datetime.now(timezone.utc)
        db.execute(
            """
            INSERT INTO posts
                (user_id, image_path, caption, timestamp)
            VALUES
                (:user_id, :image_path, :caption, :timestamp)
            """,
            user_id=user_id,
            image_path=img_name_safe,
            caption=caption,
            timestamp=timestamp
        )
        db.execute("UPDATE users SET img_count = img_count + 1 WHERE id=?", user_id)
    except Exception:
        return "db Error."
    return redirect(url_for("profile"))


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect(url_for("feed"))


@app.route("/profile")
@login_required
def profile():
    user_id = session["user_id"]
    try:
        posts = db.execute(
            """
            SELECT id, image_path, caption, timestamp FROM posts
            WHERE user_id = :user_id
            ORDER BY timestamp DESC
            """,
            user_id=user_id)
    except Exception:
        return "DB Error. Couldn't retrieve any of your posts."
    return render_template("profile.html", posts=posts)


@app.route("/delete", methods=["GET", "POST"])
@login_required
def delete():
    if request.method == "GET":
        return redirect(url_for("profile"))
    post_id = request.form.get("post_id")
    user_id = session["user_id"]
    if not post_id:
        return redirect(url_for("profile"))
    try:
        db.execute(
            "DELETE FROM posts WHERE id = :id AND user_id = :user_id",
            id=post_id,
            user_id=user_id
        )
        db.execute(
            "UPDATE users SET img_count = img_count - 1 WHERE id = :id",
            id=user_id
        )
    except Exception:
        return "DB Error."
    return redirect(url_for("profile"))


@app.route("/finder")
@login_required
def finder():
    user_id = session["user_id"]
    try:
        users = db.execute(
            """
            SELECT id, name, username, img_count FROM users
            WHERE id != ?
            ORDER BY username
            """,
            user_id
        )

        selected_user_ids = db.execute(
            "SELECT selected_user_id FROM filter WHERE user_id = ?",
            user_id
        )
        # Convert the list of dictionaries to a list of integers
        selected_user_ids = [row["selected_user_id"] for row in selected_user_ids]
    except Exception:
        return "DB Error. Couldn't retrieve usernames / filters."

    return render_template("finder.html", users=users, selected_user_ids=selected_user_ids)


# <...> is a variable that is taken from URL & is fed to the function just below.
# <int: user_id> converts user_id input to integer. Final URL generated is: profile/user_id
@app.route("/public-profile/<int:user_id>")
@login_required
def public_profile(user_id):
    try:
        posts = db.execute(
            """
            SELECT id, image_path, caption, timestamp FROM posts
            WHERE user_id = :user_id
            ORDER BY timestamp DESC
            """,
            user_id=user_id)
        user = db.execute(
            "SELECT name, username FROM users WHERE id = ?",
            user_id
        )
        user = user[0]
    except Exception:
        return f"DB Error. Couldn't retrieve any of {user_id}'s posts."
    return render_template("public-profile.html", posts=posts, user=user)


@app.route("/delete-profile", methods=["GET", "POST"])
@login_required
def delete_profile():
    if request.method == "GET":
        return render_template("delete-profile.html")
    user_id = session["user_id"]

    # Mind the order of deletion. Delete from tables with FOREIGN KEY 1st or face errors.
    try:
        db.execute("DELETE FROM likes WHERE user_id = ?", user_id)
        db.execute("DELETE FROM likes WHERE post_id IN (SELECT id FROM posts WHERE user_id = ?)", user_id)
        db.execute("DELETE FROM filter WHERE user_id = ? OR selected_user_id = ?", user_id, user_id)
        db.execute("DELETE FROM posts WHERE user_id = ?", user_id)
        db.execute("DELETE FROM users WHERE id = ?", user_id)
    except Exception:
        return "DB Error. Couldn't delete profile."

    session.clear()
    return render_template("profile-deleted.html")


@app.route("/filter", methods=["POST"])
@login_required
def filter():
    user_id = session["user_id"]
    # Get list of all selected_user_ids from finder page
    selected_user_ids = request.form.getlist("user_ids")
    try:
        # Remove any existing filters first & then insert fresh filters
        db.execute(
            "DELETE FROM filter WHERE user_id = ?",
            user_id
        )

        # Insert fresh filters if the user selected at least one
        if selected_user_ids:
            # Convert each id in list to int
            selected_user_ids = [int(selected_user_id) for selected_user_id in selected_user_ids]
            for selected_user_id in selected_user_ids:
                db.execute(
                    "INSERT INTO filter (user_id, selected_user_id) VALUES (?, ?)",
                    user_id,
                    selected_user_id
                )
    except Exception:
        return "DB Error. Filter failed."
    return redirect(url_for("feed"))
