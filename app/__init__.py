from email.policy import default
from xmlrpc.client import DateTime
from dotenv import load_dotenv
import os
import datetime
from flask import Flask, render_template, request
from peewee import *
from playhouse.shortcuts import model_to_dict
from .fellow_nav import fellow_nav

load_dotenv()
app = Flask(__name__)


if os.getenv("TESTING") == "true":
       print("Running in test mode")
       mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
       mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
              user=os.getenv("MYSQL_USER"),
              password=os.getenv("MYSQL_PASSWORD"),
              host=os.getenv("MYSQL_HOST"),
              port=3306
              )       

print(mydb)

class TimelinePost(Model):
       name = CharField()
       email = CharField()
       content = TextField()
       created_at = DateTimeField(default=datetime.datetime.now)

       class Meta:
              database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

app.register_blueprint(fellow_nav, url_prefix='/')

@app.route('/')
def home():
    """ Landing Page """
    nav = [{'name': 'Home', 'url': '/'},
           {'name': 'Kristen', 'url': '/kristen'},
           {'name': 'Helen', 'url': '/helen'},
           {'name': 'Catherine', 'url': '/catherine'}]
    return render_template('home.html', nav=nav, title="MLH Fellow", url=os.getenv("URL"))

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

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():

       if (not 'name' in request.form):
              return "Invalid name", 400
       
       content = request.form['content']
       if (content == ''):
              return "Invalid content", 400
       
       name = request.form['name']
       email = request.form['email']

       if "@" not in email:
              return "Invalid email", 400

       
       timeline_post = TimelinePost.create(name=name, email=email, content=content)

       return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
       return {
              'timeline_posts': [
                     model_to_dict(p)
                     for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
              ]
       }

@app.route('/api/timeline_post', methods=['DELETE'])
def delete_time_line_post():
       id = request.form['id']
       sql = TimelinePost.delete().where(TimelinePost.id == id)
       sql.execute()

       return {
              'timeline_posts': [
                     model_to_dict(p)
                     for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
              ]
       }

@app.route('/timeline')
def timeline():
       # creating a variable to loop through the posts and assign
       posts = [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())]
       return render_template('timeline.html', title="Timeline", posts=posts)
          