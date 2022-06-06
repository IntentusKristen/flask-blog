import os
from flask import Flask, render_template, make_response
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
from .fellow_nav import fellow_nav

app.register_blueprint(fellow_nav, url_prefix='/')


@app.route('/')
def home():
    """ Landing Page """
    nav = [{'name': 'Home', 'url': '/'},
           {'name': 'Kristen', 'url': '/kristen'},
           {'name': 'Helen', 'url': '/helen'},
           {'name': 'Catherine', 'url': '/catherine'}]
    return render_template('home.html', nav=nav, title="MLH Fellow Orientation Hack", url=os.getenv("URL"))

@app.route('/catherine/hobbies')
def catherine_hobbies():
    """ Catherine's Hobbies Page """
    nav = [{'name': 'Home', 'url': '/'},
           {'name': 'Kristen', 'url': '/kristen'},
           {'name': 'Helen', 'url': '/helen'},
           {'name': 'Catherine', 'url': '/catherine'}]

    hobbies = [{
           'name': 'Games',
           'img': '../static/img/catherine/gaming.jpg',
           'desc': 'I play a lot of games in my free time. Some of the games I have the most hours for or play the most are: Valorant, League of Legends, and Destiny 2'
    },{
           'name': 'Choir',
           'img': '../static/img/catherine/choir.jpg',
           'desc': "I've been actively involved in school choir throughout highschool and plan to continue that through college :)"
    },{
           'name': 'Hackathons',
           'img': '../static/img/catherine/coding.jpg',
           'desc': "I've won several hackathons in the past and actually found this program through hackathons. It's a fun past time and I get prizes when I win!"
    }]

    return render_template('./catherine/catherine_hobbies.html', nav=nav, hobbies=hobbies, title="Catherine's Hobbies", url=os.getenv("URL"))

@app.route('/kristen/hobbies')
def kristen_hobbies():
    return render_template('kristen_hobbies.html', title="My Hobbies", url=os.getenv("URL"))

