#session is new, for safty reaseons, session: global variable, so I can use it everywhere, otherhand: 
# fancy enough it is tied to the current user, so even if all of us on zoom right now, using my URL, 
# each of us is getting our own copy of a variable called "session", its implemented underneath the 
# hood by way of this cookie mechanism. Each of us, when you visit my application are getting a 
# different cookie value, that cookie value is like mapping to different hanger in the closet, so my 
# data will go on that hanger, your date will go on that hanger. the hanger is going to be where all of 
# our individual data is stored, what do we wanna store, per example: user name
# session is implemented be Flask for us, in such a way that each of us as users get our own version thereof (davon, hiervon, daraus)

from flask import Flask, redirect, render_template, request, session # every user got the own copy of session, cookie identifier
from flask_session import Session # Library which enables handstamps for app(Nesselbach), reminds the browser 
#to led user on the webpage as he logged in before, also when browser tabs where closed before (see google mail), nice cookies

app = Flask (__name__) 
# some lines for documentation to configure flask_session (application)
app.config ["SESSION_PERMANENT"] = False # specificly only to library called Flask session
app.config ["SESSION_TYPE"] = "filesystem" # alternative of DB using, configure flask session use the file system (fancy for =hard drive of computer or own IDE account)
Session(app) # only boilerplate (Textbausteine), 3 lines copied from documentation for the library flask_session

# To use the flask_session Library (same for Mail Library) we need another file "requirements"
# for installation of the packages in the whole (pip)

@app.route("/")
def index():
    if not session.get("name"): # if there is no name in the session
        return redirect("/login") # send user to login
    return render_template("index.html") # otherwise go ahead and render the tmp index.html, route with funktion "index", which opens by default template "index.html"


@app.route("/login", methods=["GET", "POST"]) # POST for privacy, GET render template index, login as needed
def login():
    if request.method == "POST":  # from login form
        # Remember that user logged in
        # name = request.form.get("name") # I wanna store users name in a session, as soon we have the handstamp, it´s like a coat check (Garderrobenmarke) too, like a identifier (=number)
        # same as in ther world of webbrowsers, when you get a unique cookie (giving you a coat number), where all the code can go,
        # especially for variables, we want to remeber
        # Thanks to Flask we have access to, but really thanks to http, we have acces to this special Variable called "session" (Library see on import above) 
        # Redirect user to /
        # session ["name"] = name # use this session as dictionary in Python, add users name as "name" 
        # browser represents name of cookie, that why browser remembers me no matter if I close the tab, or log out
        # easier
        # put users name in session 
        session["name"] = request.form.get("name") # "name" = users name, put the usersname in a session (special coat hanger = identifier), the key of ["name"] and value (request.form.get("name")) of whatever the user logged
        return redirect("/")
    return render_template("login.html") # same for login route

@app.route("/logout")
def logout():
    session ["name"] = None # forget the the user logged in - simplest version= just change users name to "None"
    return redirect("/")

