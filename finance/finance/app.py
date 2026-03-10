import os

from cs50 import SQL
from datetime import datetime, timezone
from flask import Flask, flash, redirect, render_template, request, session, jsonify, url_for
from functools import wraps
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


@app.route("/", endpoint = "index") # Manually defining endpoints.
@login_required
def index():
    """Show portfolio of stocks"""
    user_id=session["user_id"]
    rows = db.execute(
        """
        SELECT symbol, SUM(shares) AS shares FROM transactions
        WHERE user_id = :id
        GROUP by symbol
        HAVING SUM(shares) > 0
        """,
        id=user_id
    )
    total_portfolio = 0
    for row in rows:
        symbol = row["symbol"]
        query = lookup(symbol)
        price = query["price"]
        shares = row["shares"]
        total = shares * price
        row["current_price"] = price
        row["total"] = total
        total_portfolio = total_portfolio + total

    cash = db.execute(
        "SELECT cash FROM users WHERE id = :id",
        id=user_id
    )
    cash = cash[0]["cash"]
    total = cash + row["total"]
    return render_template("index.html", rows=rows, cash=cash, total_portfolio=total_portfolio)


@app.route("/get_portfolio_data") # A new endpoint for our JavaScript to call
@login_required
def get_portfolio_data():
    """Returns current portfolio data as JSON for AJAX updates."""

    user_id = session["user_id"]

    # 1. Get current stock holdings (Net shares: Buys - Sells)
    rows = db.execute(
        """
        SELECT symbol, SUM(shares) AS shares FROM transactions
        WHERE user_id = :id
        GROUP by symbol
        HAVING SUM(shares) > 0
        """,
        id=user_id
    )

    # Prepare a list to hold stock data for JSON response
    stocks_data = []
    current_total_stocks_value = 0 # To recalculate total portfolio value.

    # 2. Add current price and total value for each stock holding
    for row in rows:
        symbol = row["symbol"]
        stock_info = lookup(symbol)

        current_price = "N/A"
        total_stock_value_for_row = "N/A"
        if stock_info: # Check if lookup was successful
            current_price = stock_info["price"]
            total_stock_value_for_row = row["shares"] * current_price
            current_total_stocks_value += total_stock_value_for_row # Add to running total

        # Store data in a dictionary for this stock
        stocks_data.append({
            "symbol": symbol,
            "shares": row["shares"],
            "current_price": current_price,
            "total_stock_value": total_stock_value_for_row
        })

    cash_data = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
    cash = cash_data[0]["cash"]
    total_portfolio_value = current_total_stocks_value + cash
    # 5. Return all data as JSON
    # jsonify automatically converts Python lists/dictionaries into JSON format
    return jsonify({
        "stocks": stocks_data,
        "cash": cash,
        "total_portfolio_value": total_portfolio_value
    })


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    symbol = request.form.get("symbol").strip()
    quantity = request.form.get("shares").strip()
    if not symbol or \
        not quantity:
        return apology("Symbol & Quantity can't be blank")
    try:
        quantity = int(quantity)
    except ValueError:
        return apology("Invalid Quantity.")
    if quantity <= 0:
        return apology("Quantity has to be more than 0.")
    info = lookup(symbol)
    if not info:
        return apology("Symbol not found.")
    price = info["price"]
    cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
    if not cash:
        return "Invalid cash."
    cash = cash[0]["cash"]
    total = price * quantity
    if cash < total:
        return apology("Not enough muneh.")
    updated_cash = cash - total
    try:
        timestamp = datetime.now(timezone.utc)
        # Update transactions
        db.execute(
            """
            INSERT INTO transactions
                (user_id, symbol, shares, price, total, type, timestamp)
            VALUES
                (:user_id, :symbol, :shares, :price, :total, :type, :timestamp)
            """,
            user_id=session["user_id"],
            symbol=symbol,
            shares=quantity,
            price=price,
            total=total,\
            type="BUY",
            timestamp=timestamp
        )
        # Update cash
        db.execute(
            "UPDATE users SET cash = :cash WHERE id = :user_id",
            cash=updated_cash,
            user_id=session["user_id"]
        )
        return redirect("/")
    except Exception as e:
        print (e)
        return apology("Error.")

    # if everything successful:
    #     return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


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
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
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
    if request.method == "GET":
        return render_template("quote.html")
    symbol = request.form.get("symbol").strip()
    if not symbol:
        return apology("Symbol can't be blank")
    info = lookup(symbol)
    if not info:
        return apology("Symbol not found")
    return render_template("quoted.html", info=info)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    username_val = request.form.get("username")
    password_val = request.form.get("password")
    confirmation_val = request.form.get("confirmation")
    if not username_val or \
    not password_val or \
    not confirmation_val or \
    password_val != confirmation_val:
        return apology("Either blank or password mismatch")
    username_val = username_val.lower()
    password = generate_password_hash(password_val)
    try:
        db.execute(
            "INSERT INTO users (username, hash) VALUES (?)",
            (username_val, password)
        )
        return redirect("/")
    except Exception as exception:
        print(exception)
        return apology("Error")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
