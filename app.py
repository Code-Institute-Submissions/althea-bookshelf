import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

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

cloudinary.config(
    cloud_name=os.environ.get('CLOUD_NAME'),
    api_key=os.environ.get('API_KEY'),
    api_secret=os.environ.get('API_SECRET')
)


# Function and route to Home Page
@app.route("/")
@app.route("/get_books")
def get_books():
    books = list(mongo.db.books.find())
    review = list(mongo.db.review.find())
    return render_template("books.html", books=books, review=review)


# Function and route to add search functionality
@app.route("/seach", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books = list(mongo.db.books.find({"$text": {"$search": query}}))
    return render_template("books.html", books=books)


# Function and route to create a new user
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
        flash("Hi {} ".format(request.form.get("username")))
        flash("Welcome to the Fun World of Children's Book")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# Function and route for user to login
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
                flash("Invalid Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exists
            flash("Invalid Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Function and route to display user's profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username in db
    angel_name = mongo.db.critics.find_one(
        {"username": session["user"]})["angel_name"].capitalize()
    angel_age = mongo.db.critics.find_one(
        {"username": session["user"]})["angel_age"]

    # grab the user's reviewed books
    books = list(mongo.db.books.find())
    username = mongo.db.books.find_one(
        {"username": session["user"]})

    if session["user"]:
        return render_template(
            "profile.html", username=username,
            angel_name=angel_name, angel_age=angel_age, books=books)

    return redirect(url_for("login"))


# Function and route to delete profile
@app.route("/delete_profile/<critics_id>")
def delete_profile(critics_id):
    # Remove session user's profile from the db
    mongo.db.critics.remove({"username": session["user"]})
    # Remove session user's books from the db
    mongo.db.books.remove({"username": session["user"]})
    flash("Profile Successfully Deleted")
    return redirect(url_for("logout"))


# Function and route for user to logout
@app.route("/logout")
def logout():
    # remove user from session cookies
    session.pop("user")
    return redirect(url_for("login"))


# Function and route to add books
@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        photo = request.files['photo_url']
        photo_upload = cloudinary.uploader.upload(photo)
        is_recommend = "on" if request.form.get("is_recommend") else "off"
        book = {
            "book_title": request.form.get("book_title"),
            "book_author": request.form.get("book_author"),
            "book_review": request.form.get("book_review"),
            "fun_meter": request.form.get("fun_meter"),
            "is_recommend": is_recommend,
            "date_posted": request.form.get("date_posted"),
            "username": session["user"],
            "photo_url": photo_upload["secure_url"]
        }
        mongo.db.books.insert_one(book)
        flash("Thank you for your contribution!")
        return redirect(url_for("get_books"))
    return render_template("add_books.html")


# Function and route to update book
@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        photo = request.files['photo_url']
        photo_upload = cloudinary.uploader.upload(photo)
        is_recommend = "on" if request.form.get("is_recommend") else "off"
        review = {
            "book_title": request.form.get("book_title"),
            "book_author": request.form.get("book_author"),
            "book_review": request.form.get("book_review"),
            "fun_meter": request.form.get("fun_meter"),
            "is_recommend": is_recommend,
            "date_posted": request.form.get("date_posted"),
            "username": session["user"],
            "photo_url": photo_upload["secure_url"]
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, review)
        flash("Book review is updated!")
        return redirect(url_for("get_books"))

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("edit_book.html", book=book)


# Function and route to delete a book
@app.route("/remove_book/<book_id>")
def remove_book(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Book Successfully Removed")
    return redirect(url_for("get_books"))


# Function and route for the user to add review on a book
@app.route("/add_review/<book_id>", methods=["GET", "POST"])
def add_review(book_id):
    # Get the ID of the book the user wants to review
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    if request.method == "POST":
        # New review is saved in the correct format
        new_review = {
            "title": book["book_title"],
            "user_review": request.form.get("user_review"),
            "username": session["user"]
        }
        # Review is added
        mongo.db.review.insert_one(new_review)
        flash("Review Added")
        return redirect(url_for("get_books"))

    return render_template("add_review.html", book=book)


# Function and route to delete a book review
@app.route("/remove_review/<review_id>")
def remove_review(review_id):
    mongo.db.review.remove({"_id": ObjectId(review_id)})
    flash("Book Successfully Removed")
    return redirect(url_for("get_books"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
