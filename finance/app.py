import os
import datetime
import pytz

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, check_card

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


# Default method is get


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Get the shares information that will be exhibited
    shares_info = db.execute(
        "SELECT symbol, quantity FROM shares WHERE user_id = ?", session["user_id"]
    )

    # Get the share price and total value
    for dict in shares_info:
        price = lookup(dict["symbol"])
        price = price["price"]
        dict["price"] = price
        dict["total"] = round(dict["quantity"] * dict["price"], 2)

    # Get the user cash and calculate the their account value (cash + shares value)
    total_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    total_cash = round(total_cash[0]["cash"], 2)
    total_value = round(total_cash + sum(dict["total"] for dict in shares_info), 2)

    return render_template(
        "index.html",
        shares_info=shares_info,
        total_cash=total_cash,
        total_value=total_value,
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # If user gets by post (submitted form)
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # If any field are empty:
        if not symbol or not shares:
            return apology("Symbol and shares are required!")

        # If shares is not a positive integer
        try:
            float_share = float(shares)
            if float_share != int(float_share) or float_share < 1:
                return apology("Invalid share")
        except ValueError:
            return apology("Invalid share")

        # Convert shares to an int
        shares = int(shares)

        # If succeeds contains a dict with price and symbol keys.
        share_data = lookup(symbol)
        # If symbol is invalid:
        if not share_data:
            return apology("Invalid symbol")

        # Get the user cash amount
        user_cash = db.execute(
            "SELECT cash FROM users WHERE id = ?", session["user_id"]
        )
        user_cash = float(user_cash[0]["cash"])

        # Get the purchase amount
        total_amount = shares * share_data["price"]
        # See if user has enough cash to proceed with the purchase
        if total_amount > user_cash:
            return apology("Can't afford that!")

        # Discount the money from the user
        user_cash = user_cash - total_amount
        # Update the users table (cash)
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", user_cash, session["user_id"]
        )

        # Update the shares table with the new shares data
        # Verify if the user already have shares of this type
        symbol_check = db.execute(
            "SELECT symbol FROM shares WHERE user_id = ? AND symbol = ?",
            session["user_id"],
            share_data["symbol"],
        )

        print(symbol_check)
        # If not, should be created
        if not symbol_check:
            db.execute(
                "INSERT INTO shares (user_id, symbol, quantity) VALUES(?, ?, ?)",
                session["user_id"],
                share_data["symbol"],
                shares,
            )

        # Otherwise just update the existing share
        else:
            db.execute(
                "UPDATE shares SET quantity = quantity + ? WHERE user_id = ? AND symbol = ?",
                shares,
                session["user_id"],
                share_data["symbol"],
            )

        # Update the transactions table
        current_time = datetime.datetime.now(pytz.timezone("UTC"))
        db.execute(
            "INSERT INTO transactions (user_id, symbol, type, quantity, price, date) VALUES(?, ?, ?, ?, ?, ?)",
            session["user_id"],
            share_data["symbol"],
            "Buy",
            shares,
            share_data["price"],
            current_time,
        )

        flash("Bought!")
        return redirect("/")

    # If user reaches by get (navbar/url)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    if request.method == "GET":
        history_data = db.execute(
            "SELECT symbol, type, quantity, price, date FROM transactions WHERE user_id = ? ORDER BY date DESC",
            session["user_id"],
        )
        return render_template("history.html", history_data=history_data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password")

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

    # If user reached via post
    if request.method == "POST":

        symbol = request.form.get("symbol")

        # if symbol empty
        if not symbol:
            return apology("Stock symbol is required!")

        # Lookup returns a dict with keys (price, symbol) or None
        quote_data = lookup(symbol)

        # If lookup returns none
        if not quote_data:
            return apology("Invalid stock symbol")

        # If api request was succesful:
        return render_template(
            "quoted.html",
            input=symbol,
            price=quote_data["price"],
            symbol=quote_data["symbol"],
        )

    # If user reached via get
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # If user reached this route via post (submitted the registration form)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Check empty fields
        if not username or not password or not confirmation:
            return apology("Username, password and confirmation fields are required!")

        # If password does not match
        if password != confirmation:
            return apology("Passwords do not match")

        # Hashing the password with the default hash to insert in the database (pbkdf2:sha256:600000)
        password_hash = generate_password_hash(password)

        # Insert the new user in the database (users)
        try:
            # If insert operation is succesfull, it returns the primary key of the registration inserted.
            primary_key = db.execute(
                "INSERT INTO users (username, hash) VALUES(?, ?)",
                username,
                password_hash,
            )
        # If username already exists
        except ValueError:
            return apology("Username not available :(")

        # If registration succeed, automatically establish a login session
        session["user_id"] = primary_key

        flash("Registration completed, Welcome!")
        return redirect("/")

    # If user reached this route via get (clicked the navbar registration or typed the url)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # If user sends the form to sell a stock
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Check if it is a valid symbol
        user_shares = db.execute(
            "SELECT symbol, quantity FROM shares WHERE user_id = ?", session["user_id"]
        )
        list_shares = [dict["symbol"] for dict in user_shares]
        if symbol not in list_shares:
            return apology("Invalid symbol")

        # Check if it is a valid number of shares
        try:
            float_share = float(shares)
            if float_share != int(float_share) or float_share < 1:
                return apology("Invalid share number")
        except ValueError:
            return apology("Invalid share number")

        # Check if user has enough shares, create boolean to check if registry should be deleted, get share new quantity
        new_quantity = 0
        all_shares_sold = False
        shares = int(shares)
        for dict in user_shares:
            if dict["symbol"] == symbol:
                if dict["quantity"] < shares:
                    return apology("Not enough shares")
                if dict["quantity"] == shares:
                    all_shares_sold = True
                    new_quantity = 0
                else:
                    new_quantity = dict["quantity"] - shares

        # Update the shares table registry
        db.execute(
            "UPDATE shares SET quantity = ? WHERE user_id = ? AND symbol = ?",
            new_quantity,
            session["user_id"],
            symbol,
        )

        # Update the users table cash column
        share_value = lookup(symbol)
        share_value = share_value["price"]
        user_cash = db.execute(
            "SELECT cash FROM users WHERE id = ?", session["user_id"]
        )
        user_cash = user_cash[0]["cash"]
        update_cash = user_cash + (share_value * shares)
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", update_cash, session["user_id"]
        )

        # If user selled all his shares, delete the registry from the table
        if all_shares_sold:
            db.execute(
                "DELETE FROM shares WHERE user_id = ? AND symbol = ?",
                session["user_id"],
                symbol,
            )

        # Create the transaction registry
        current_time = datetime.datetime.now(pytz.timezone("UTC"))
        db.execute(
            "INSERT INTO transactions (user_id, symbol, type, quantity, price, date) VALUES(?, ?, ?, ?, ?, ?)",
            session["user_id"],
            symbol,
            "Sell",
            shares,
            share_value,
            current_time,
        )

        flash("Sold!")
        return redirect("/")

    # If user just accessed the sell page
    else:
        user_shares = db.execute(
            "SELECT symbol FROM shares WHERE user_id = ?", session["user_id"]
        )
        return render_template("sell.html", user_shares=user_shares)


@app.route("/pwchange", methods=["GET", "POST"])
@login_required
def pwchange():
    if request.method == "POST":
        old = request.form.get("old")
        new = request.form.get("new")
        confirmation = request.form.get("confirmation")

        if not old or not new or not confirmation:
            return apology("All fields are required")

        if new != confirmation:
            return apology("Passwords do not match")

        # Get the password hashing and compare to see if its correct
        current = db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])
        current = current[0]["hash"]
        validation = check_password_hash(current, old)
        if not validation:
            return apology("Incorrect password")

        # Generate hash for the new password
        new_password = generate_password_hash(new)

        # Update the user password(hash) in users table
        db.execute("UPDATE users SET hash = ? WHERE id = ?", new_password, session["user_id"])

        flash("Password changed!")
        return redirect("/")

    else:
        return render_template("pwchange.html")


@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    if request.method == "POST":
        value = request.form.get("value")
        method = request.form.get("method")
        card = request.form.get("card")

        # If the default fields are empty
        if not value or not method:
            return apology("Amount and method are required")

        # If card method is chosen but no card is provided
        if method != 'deposit' and not card:
            return apology("Card number is required")

        # If value is valid
        try:
            float_value = float(value)
            if float_value != int(float_value) or float_value <= 0:
                return apology("Invalid amount")
        except ValueError:
            return apology("Invalid amount")
        value = float(value)

        # Get time of the transaction
        current_time = datetime.datetime.now(pytz.timezone("UTC"))

        # Insert the money if the method is deposit
        if method == 'deposit':
            db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", value, session["user_id"])
            # Update transaction table
            db.execute(
                "INSERT INTO transactions (user_id, symbol, type, quantity, price, date) VALUES(?, ?, ?, ?, ?, ?)",
                session["user_id"],
                "CASH",
                "Deposit",
                0,
                value,
                current_time,
            )
            flash("Successful deposit!")
            return redirect("/")

        # Check if card number is valid
        if not check_card(method, card):
            return apology(f"Invalid {method} card")

        # Insert the money in users(cash)
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", value, session["user_id"])
        # Update transaction table
        db.execute(
            "INSERT INTO transactions (user_id, symbol, type, quantity, price, date) VALUES(?, ?, ?, ?, ?, ?)",
            session["user_id"],
            "CASH",
            "Deposit",
            0,
            value,
            current_time,
        )

        flash("Successful deposit!")
        return redirect("/")

    else:
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = cash[0]["cash"]
        methods_list = ["amex", "visa", "mastercard", "deposit"]
        return render_template("deposit.html", cash=cash, methods=methods_list)
