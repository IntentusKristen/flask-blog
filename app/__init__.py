import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
from .fellow_nav import fellow_nav
from .k_hobbies import k_hobbies

app.register_blueprint(fellow_nav, url_prefix='/')
app.register_blueprint(k_hobbies, url_prefix='/kristen/')


@app.route('/')
def home():
    """ Landing Page """
    nav = [{'name': 'Home', 'url': '/'},
           {'name': 'Kristen', 'url': '/kristen'},
           {'name': 'Helen', 'url': '/helen'},
           {'name': 'Catherine', 'url': '/catherine'}]
    return render_template('home.html', nav=nav, title="MLH Fellow Orientation Hack", url=os.getenv("URL"))

@app.route('/kristen/hobbies')
def kristen_hobbies():
    return render_template('kristen_hobbies.html', title="My Hobbies", url=os.getenv("URL"))
