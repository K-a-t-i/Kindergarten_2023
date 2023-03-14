from cs50 import SQL
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///shows.db")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    shows = db.execute("SELECT * FROM shows WHERE title LIKE ?", "%" + request.args.get("q") + "%") # request.args.get("q") is users search, per exp. alle movies/shows with "office" in the name, "%" = sql wildcard placeholders - zero or more characters to the left and right - thats why we getting matches with "office" at the beginning, middle and end of the  word
    #return render_template("search.html", shows=shows)
    return jsonify(shows) # json: javaScript Object Notation, standatised format for transmitting data between servers and browsers, using a very lightweight text format/ jsonify: Flask function that takes a Python list or dictionary and converts it into json format
    # returning the jsonification of the shows variable, which recall is just the rows that came back from db.exe, dictionary = object in javaScript
    # browser convert json file (only text, , [], {}) into html
    # js mutate or change dom - the document object model - the tree in memory, with js you add more nodes to that tree


# IDs, title of tv shows
# Terminal
# sqlite .schema
# CREATE TABLE shows (id INTEGER, title TEXT NOT NULL, PRIMARY KEY(id))
# infromation is send of web using python and javaScript
