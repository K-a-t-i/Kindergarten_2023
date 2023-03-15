import os # os (operating system) gives you access to the env variables (property files) and others, where you can store secure stuff like email addresses and passwords
from cs50 import SQL # import DB: CS50 Library, SQL Library - You have to create DB on own? - Create Table "Registrans" with Columns: id (Int), name (Text not null), sport (text not null), Primary Key (id)
from flask import Flask, redirect, render_template, request  # import from flask the Flask function itself, render_template (call all templates), request, redirect (3.0.1, or other status code, location of the browser, go here instead)
from flask_mail import Mail, Message # Libray: import Mail for sending regestriant a confirmation mail

# bunch of initalisation step to write Python code to generate emails to registrans programmatically  
app = Flask(__name__) # initialise the application with this Flask function using name
# lot of setting for mailserver #os.getenw = property files = privat keep it save in a other environment (variable) or file witch it not reachable from client
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER") # Default Sender revers to default email address, or =my email= kati.rupp@...; getenv is variable is defind elsewhere in IDE or Linux system 
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD") #lots of settings for mail server, password should also not shown, thats why we also grap it from the other env
app.config["MAIL_PORT"] = 587 #gmail let you send email on TCP Port 587
app.config["MAIL_SERVER"] = "smtp.gmail.com" #you will find that on googles documentation
app.config["MAIL_USE_TLS"] = True # TLS is a typ of encryption, enable with TRUE
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME") # i dont know what user name they are taking, thats we grap this also from the env, best practise is storing secure information in env variables, not only for try out reasons use private passwords, you will send it to the server, if you run the code
mail = Mail(app) # mail variable, passing copy flask applications (=app) to a function called Mail

#REGISTRANTS = # store our registrants in a dictionary with a global CONSTANT, store name of Registrant and sport to have in computers` memory a list of all the vaild registration
# instead of the dictionary we can use a DB to store the data
#db = SQL("sqlite:///froshims.db") # Registrants go to SQL database

#in sqlite shema: CREATE TABLE registrans (id  INTEGER, name TEXT NOT NULL, sport TEXT NOT NULL, PRIMARY KEY(id))



SPORTS = [        # Variable, Capital Letters global Constant, create a list
    "Dodgeball",
    "Flag Football",
    "Soccer",
    "Volleyball",
    "Ultimate Frisbee", 
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS) #render a template called index.html/ Variable sports have the Value of the global Constant SPORTS, which is a list put in index template

@app.route("/register", methods=["POST"])
def register():
    email = request.form.get("email") # get users email from the form, variable name/email, actually register the registrants, not only saying it on html, activly store on server the data (name of registrants   )
    if not email:
        return render_template("error.html", message="Missing email")

    sport = request.form.get("sport") # variable sports, actually register the registrants, not only saying it on html, activly store on server the data (sport of registrants)
    if not sport:
        return render_template("error.html", message="Missing sport")

    if sport not in SPORTS: # if variable sport not in global constant SPORTS
        return render_template("error.html", message="Invalid sport") # manually typed in, sport is not on server (not in global variable, not in list)

    #REGISTRANTS[name] = sport  # keys and values, name to index into the Python dictionray and setting the value equal to sport computers memory recall using by way of this global variable called REGISTRANTS (all caps to make clear that it is a global variable) - successful restistration - register the user, i want to remember, that the registrant is registered for a given sport in the computer memory - with name and sport

    # return render_template("registrants.html", registrants=REGISTRANTS) # like with the sports variable, providing my registrants.html (template) with a variable called registrants setting it equal to the value of that global variable thereby giving my template access to that dictionary, ability to save all these registrants to a global variable

    #if not request.form.get("name") or request.form.get("sport") not in SPORTS:  # Error checking, Type Name and Sport, Sport must be in Constant SPORT (=list), if not template failure will appear
        #return render_template("failure.html") # give a failure, if typed in no name or sports
    #return
    #  render_template("success.html") #presume the registration would be succesful
# register registrans
   # db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport) #insert name and sport in db

    message = Message("You are registered!", recipients=[email])  # send this to massage is variable, Massage is feature imported at the top of here, second Argument recipient
    mail.send(message) # dynamic generated emails to gmail, if you registered

    return render_template("succes.html")
    #return redirect("/registrants") # redirect the user to /registrants html, so that the registrants see themself and others; URL .../registrans


#@app.route("/registrants") # iterrating over table row of registrans
#def registrants():
    #registrants = db.execute("SELECT * FROM registrants") # getting back tablerows, each row is a dictonary of columns and he values there are in # query, access to all registrants from DB, registrans getting back rows of data
   # return render_template("registrants.html", registrants=registrants)  # name of variable = name want to use in template; return registrants from html, before =REGISTRANTS from veriable

# fully fledged web application, own db with sqlite, own templates dynamically generating a table on registrants template, beautify with some css or bootstrap


