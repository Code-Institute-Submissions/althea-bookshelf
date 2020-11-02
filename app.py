import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_books")
def get_books():
    books = list(mongo.db.books.find())
    return render_template("books.html", books=books)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username is already exists in db
        existing_user = mongo.db.critics.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "angel_name": request.form.get("angel_name").lower(),
            "angel_age": request.form.get("angel_age")
        }
        mongo.db.critics.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        flash("Hi {} ".format(request.form.get("angel_name")))
        flash("Welcome to the Fun World of Children's Book")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.critics.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches the user input
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back!". format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))

            else:
                # invalid password match
                flash("incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exists
            flash("incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username in db
    username = mongo.db.critics.find_one({"username": session["user"]})["username"].capitalize()
    angel_name = mongo.db.critics.find_one({"username": session["user"]})["angel_name"].capitalize()
    angel_age = mongo.db.critics.find_one({"username": session["user"]})["angel_age"]

    if session["user"]:
        return render_template(
            "profile.html", username=username,
            angel_name=angel_name, angel_age=angel_age)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        is_recommend = "on" if request.form.get("is_recommend") else "off"
        book = {
            "book_title": request.form.get("book_title"),
            "book_author": request.form.get("book_author"),
            "book_review": request.form.get("book_review"),
            "fun_meter": request.form.get("fun_meter"),
            "is_recommend": is_recommend,
            "date_posted": request.form.get("date_posted"),
            "fun_viewed": session["user"]
        }
        mongo.db.books.insert_one(book)
        flash("Thank you for your contribution!")
        return redirect(url_for("get_books"))
    return render_template("add_books.html")


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("edit_book.html", book=book)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)