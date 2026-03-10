import os

from cs50 import SQL
from datetime import datetime
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    make_response,
)
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Fetch user data (cash balance and stock transactions)
    user = db.execute("SELECT id, cash FROM users WHERE id = (?);", session["user_id"])[
        0
    ]
    rows = db.execute(
        "SELECT symbol, SUM(shares) AS shares FROM transactions WHERE user_id = (?) GROUP BY symbol;",
        session["user_id"],
    )

    # Calculate total value of each stock holding
    for row in rows:
        stock = row["symbol"]
        # Get current stock price
        stock_info = lookup(stock)
        row["price"] = stock_info["price"]
        row["total_value"] = row["shares"] * stock_info["price"]

    # Calculate overall portfolio value (stocks + cash)
    total_portfolio_value = user["cash"] + sum(row["total_value"] for row in rows)

    return render_template(
        "index.html",
        stocks=rows,
        cash_balance=user["cash"],
        total_portfolio_value=total_portfolio_value,
    )
    # return apology("TODO", 200)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        stock = request.form.get("symbol")
        if lookup(stock) is None:
            return apology("Stock not found")

        # Check if quantity is positive
        quantity = request.form.get("shares")
        while True:
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    return apology("Enter a positive integer")
                else:
                    break
            except ValueError:
                return apology("Enter a positive integer")
        price = float(lookup(stock)["price"])
        total_bill = price * quantity
        cash = float(
            db.execute("SELECT cash FROM users WHERE id= :id;", id=session["user_id"])[
                0
            ]["cash"]
        )
        current_timestamp = datetime.now()
        if total_bill > cash:
            return apology("Insufficient balance")

        # Everything set & ready to buy now
        updated_cash = cash - total_bill
        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price, timestamp) VALUES (?, ?, ?, ?, ?)",
            session["user_id"],
            stock.upper(),
            quantity,
            price,
            current_timestamp,
        )
        db.execute(
            "UPDATE users SET cash = (?) WHERE id = (?)",
            updated_cash,
            session["user_id"],
        )
        return redirect("/")

    if request.method == "GET":
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    rows = db.execute(
        "SELECT * FROM transactions WHERE user_id = (?) ORDER BY timestamp;",
        session["user_id"],
    )
    return render_template("history.html", stocks=rows)
    # return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        stock = request.form.get("symbol")
        if lookup(stock) is None:
            return apology("Stock not found")
        else:
            stock_quote = lookup(stock)
            return render_template(
                "quoted.html", symbol=stock_quote["symbol"], price=stock_quote["price"]
            )
    if request.method == "GET":
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username1 = request.form.get("username")
        if not username1:
            return apology("Enter a username", 400)

        # try to add username to db.
        print(f"{username1}, tempPass")
        try:
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?);",
                (username1, "tempPass"),
            )
        except ValueError:
            return apology("Username already registered", 400)

        # ensure password is entered
        password1 = request.form.get("password")
        confirmation1 = request.form.get("confirmation")
        if not password1:
            db.execute("DELETE FROM users WHERE username = (?);", username1)
            return apology("Enter a password", 400)
        if not confirmation1 or password1 != confirmation1:
            db.execute("DELETE FROM users WHERE username = (?);", username1)
            return apology("Passwords do not match", 400)
        db.execute(
            "UPDATE users SET hash = (?) WHERE username = (?);",
            generate_password_hash(password1),
            username1,
        )
        return render_template("index.html")
    if request.method == "GET":
        return render_template("register.html")


@app.route("/security", methods=["GET", "POST"])
@login_required
def security():
    if request.method == "POST":
        old = request.form.get("old")
        if not old:
            return apology("Enter old password")
        old_pass = db.execute(
            "SELECT hash FROM users WHERE id = (?);", session["user_id"]
        )[0]["hash"]
        if not check_password_hash(old_pass, old):
            return apology("Old password incorrect")

        # ensure password is entered
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not password:
            return apology("Enter new password")
        if not confirmation or password != confirmation:
            return apology("Passwords do not match")
        db.execute(
            "UPDATE users SET hash = (?) WHERE id = (?);",
            generate_password_hash(password),
            session["user_id"],
        )
        return redirect("/logout")
    if request.method == "GET":
        return render_template("security.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        stock = request.form.get("symbol")
        query = db.execute(
            "SELECT symbol, SUM(shares) AS shares FROM transactions WHERE (user_id, symbol) = (?, ?) GROUP BY symbol;",
            session["user_id"],
            stock,
        )[0]

        # Ensure user doesn't somehow sell a stock that they do not own
        if not query:
            return apology("You don't own this stock")

        # Check if quantity is a positive integer
        quantity = request.form.get("shares")
        while True:
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    return apology("Enter a positive integer")
                else:
                    break
            except ValueError:
                return apology("Enter a positive integer")

        # Ensure not to sell more than user owns
        if quantity > query["shares"]:
            return apology("You don't own that many shares")
        stock_info = lookup(stock)
        price = float(stock_info["price"])
        cash = db.execute("SELECT cash FROM users WHERE id = (?);", session["user_id"])[
            0
        ]
        updated_cash = cash["cash"] + (quantity * price)
        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price, timestamp) VALUES (?, ?, ?, ?, ?);",
            session["user_id"],
            stock,
            -quantity,
            price,
            datetime.now(),
        )
        db.execute(
            "UPDATE users SET cash = (?) WHERE id = (?);",
            updated_cash,
            session["user_id"],
        )
        return redirect("/")

    if request.method == "GET":
        stocks = db.execute(
            "SELECT symbol, SUM(shares) AS shares FROM transactions WHERE user_id = (?) GROUP BY symbol;",
            session["user_id"],
        )
        print(f"{stocks}")
        return render_template("sell.html", stocks=stocks)
    # return apology("TODO")
