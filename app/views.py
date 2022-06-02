from flask import Blueprint, render_template

# this file a blueprint of our application -> Means it has a bunch of roots inside, has a bunch of URLs defined
# kind of separate our app out, don't have to have all our views defined in one file, can have them defined in multiple files
views = Blueprint('views', __name__)

# define our view
# this function will run whenever we go to the / route, whatever is inside of home() will run
@views.route('/')
def home():
    return render_template("home.html")