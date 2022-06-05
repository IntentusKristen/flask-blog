from flask import Blueprint, render_template
import os

# this file a blueprint of our application -> Means it has a bunch of roots inside, has a bunch of URLs defined
# kind of separate our app out, don't have to have all our views defined in one file, can have them defined in multiple files
fellow_nav = Blueprint('fellow_nav', __name__)

@fellow_nav.route('/kristen')
def kristen():
    return render_template('kristen_page.html', title="22.SUM.22 Fellow: Kristen Zhang", url=os.getenv("URL"))

@fellow_nav.route('/helen')
def helen():
    return "<p>Helen<p>"

@fellow_nav.route('/catherine')
def catherine():
    nav = [{'name': 'Home', 'url': '/'},
           {'name': 'Kristen', 'url': '/kristen'},
           {'name': 'Helen', 'url': '/helen'},
           {'name': 'Catherine', 'url': '/catherine'}]
    return render_template('catherine_page.html', nav=nav, title="22.SUM.22 Fellow: Catherine Laserna", url=os.getenv("URL"))