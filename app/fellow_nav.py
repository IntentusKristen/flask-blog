from flask import Blueprint, render_template
import os

# this file a blueprint of our application -> Means it has a bunch of roots inside, has a bunch of URLs defined
# kind of separate our app out, don't have to have all our views defined in one file, can have them defined in multiple files
fellow_nav = Blueprint('fellow_nav', __name__)

@fellow_nav.route('/kristen')
def kristen():
    work_info =  [{
            'name': 'Summer Research Intern',
            'location': 'Western University',
            'start_date': 'May 2022',
            'end_date': 'Present'
        },{
            'name': 'Production Engineering Fellow',
            'location': 'MLH',
            'start_date': 'May 2022',
            'end_date': 'Present'
        }]

    education_info = [{
            'name': 'Sir Frederick Banting S.S',
            'location': 'London, ON',
            'start_date': 'September 2016',
            'end_date': 'June 2020'
        },{
            'name': 'Western University',
            'location': 'London, ON',
            'start_date': 'September 2020',
            'end_date': 'Present'
        }]

    return render_template('kristen_page.html', title="22.SUM.22 Fellow: Kristen Zhang", url=os.getenv("URL"), work_info=work_info, education_info=education_info)

@fellow_nav.route('/helen')
def helen():
    return "<p>Helen Xia<p>"

@fellow_nav.route('/catherine')
def catherine():
    return "<p>Catherine<p>"