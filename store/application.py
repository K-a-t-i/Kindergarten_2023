from cs50 import SQL
from flask import Flask, render_template, request

# Configure app
app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///store.db")

# Configure sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app) 




@app.route("/")
def index():
    books = db.execute("SELECT * FROM books") #table "books" in db, we selecting * from books, to get me all the books
    return render_template("books.html", books=books) # rendering tamplate "books.html" and we passing in those books


@app.route("/cart", methods=["GET", "POST"])
def cart():

     # Ensure cart exists
    if "cart" not in session: # sessions run on the server
        session["cart"] = [] # initialise it to an empty list, so you can remeber what´s in your cart, same goes on on amazon

    # POST
    if request.method == "POST":
        id = request.form.get("id") # adding the ID to the books...
        if id:
            session["cart"].append(id) #...to my sessions cart key
        return redirect("/cart")

    # GET
    books = db.execute("SELECT * FROM books WHERE id IN (?)", session["cart"]) # WHERE the id of the book is IN (?) list of the books, list coming from session["cart"], using the session to store what we will call a shopping cart (Warenkorb), implemented via cookies underneath the hood, to give us the illusion of user specific variables, dictionaries, where you can store anything you want in there, so it looks like the session cart key is going to have a value equal to the IDs of a whole bunch of books/ (befor: use session to store everybodys name on a per user basis)
    return render_template("cart.html", books=books) # rendering cart.html template passing in the books from the database

# How do they go into the session?
# if the user submits the form to the cart -> if request.method == "POST":
# if the user posts to (/"cart") like i´m going to get the id that they´ve typed in, maybe if there is a id -> id = request.form.get("id")
# if id: and is there is in fact an ID and it´s not none
# session ["cart"].append(id): we appentthe cart, the ID of the book
# return redirect ("/cart"): redirect user to ("/cart")
        
# Terminal:
# open sqlite .schema
# CREATE TABLE books (id INTEGER, title TEXT NOT NULL, PRIMARY KEY(id));
# SELCT * FROM books;
# 1 Harry Potter and the Sorcrer's Stone
# ...


