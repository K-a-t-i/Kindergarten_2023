from flask import Flask, render_template, request # Function: Flask activates this as a web-app/
#render_template: find a file called index.html - grap it´s content - so that you can return it; 
# import from the flask library (=comes with a lot of functions), 
# import request variable for the flask library, gives access to http request form webbrowser bar
# with request flask parses URL, which is cat, which is david, everything behind ? flask parse and hands it back as variable to me

app = Flask(__name__) # Flask turn the current File into an application 
#-> webapplication who listen to Browsers requests __name__ = Variable  -> refer to the name of the current file

#@app.route("/", methods=["GET", "POST"]) # first route for form (in index.htlm); one route supports the two method=["GET"], ["POST"]
                                  # show user the form and say hello to the user as well 
                                  # What are my routs = URL / or /search, applying one function to another/ application.py = Controller
#def index(): # Funktion, Default route
    #if request.method == "GET":
       #return render_template("index.html") # world is default value, if name has no value
    # render (grap) a template called index.html, give me a variable called name(=Davide) from application.py
    # name which I want to get from the URL, name = value which plug into templates 
    # arg = argument
    # None means variable has no value
    # move name parameter (name=request.args.get("name", "world")) to greet route
    # flask render your code and forward it to the webpage, sometimes the intentations are destroyed (see right click on webpage -view), 
    # but the browser doesn´t care
    #if request.method == "POST":
        #return render_template("greet.html", name=request.form.get("first_name", "world"))

        #checking logically in my controler code: 
        # if the method came in as get (=go ahead and just display the form)
        # if the method came in as post (= go ahead and greet the user)
        # why this work: when ever you visit a webpage (google.com, harvard.edu, yale.edu), you have always been making get request
        # every request you made had the keyword get by default (in URL) in the envelope
        # get nothing to do with forms, its the default HTTP verb that´s used, whenever you just visit any URL 
        # when you using a form, you are using get as we did first or you are using post as we did second

# delete /greet route, bc of redundancy,
@app.route("/greet", methods=["POST"]) #second route is greet route, methods=["GET"] is default, read users input in textfield and send it to webpage, for: one form (index.html) could send data to this route instead
def greet(): #function, who wil be called, when the user visits /greet, naming should be easy, that is why we call the funktion=route=greet
    return render_template("greet.html", first_name=request.args.get("first_name", "world")) #get funktion, return index.html on webpage, "TODO" return TODO on webpage
    # grap a template called greet.html and give me a variable called name or default world from greet.html
    # first_name = parameter that I passing in to my template, let me get the first_name http parameter 
    # "first_name" = http parameter that I am grapping from the URL
    # .args.get = refers to the arguments in the URL
    # if you send e-mail addresses, passwords, credit card data otherwise get

    #return render_template("greet.html", first_name=request.form.get("first_name", "world"))
    # methods=["POST"] form.get don´t remember what I typed in a from like credit cart number, Name

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "world"))
    return render_template("index.html")




     

