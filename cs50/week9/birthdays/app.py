import os
import secrets

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check valid response
        name = request.form.get('name')
        month = request.form.get('month')
        day = request.form.get('day')
        if not validate_birthday(name, month, day):
            flash('Your birthday is not right')
            return redirect("/")

        # TODO: Add the user's entry into the database
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
        flash('Your birthday is now added')
        return redirect("/")
    else:
        # First, in app.py, add logic in your GET request handling to query the birthdays.db database for all birthdays.
        # Pass all of that data to your index.html template.
        birthdays = db.execute("SELECT * FROM birthdays")

        # TODO: Display the entries in the database on index.html
        return render_template("index.html", birthdays=birthdays)


def validate_birthday(name, month, day):
    if not name:
        return False
    if not month:
        return False
    if not day:
        return False
    try:
        month = int(month)
        if month not in range(1, 13):
            return False
    except ValueError:
        return False
    try:
        day = int(day)
        if day not in range(1, 32):
            return False
    except ValueError:
        return False
    if (month in [1, 3, 5, 7, 9, 11]) and (day > 31):
        return False
    elif (month in [4, 6, 8, 10, 12]) and (day > 30):
        return False
    elif (month == 2) and (day > 29):
        return False
    else:
        return True
