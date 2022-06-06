from flask import Blueprint, render_template
import os

# this file a blueprint of our application -> Means it has a bunch of roots inside, has a bunch of URLs defined
# kind of separate our app out, don't have to have all our views defined in one file, can have them defined in multiple files
fellow_nav = Blueprint('fellow_nav', __name__)

# nav
nav = [{'name': 'Home', 'url': '/'},
           {'name': 'Kristen', 'url': '/kristen'},
           {'name': 'Helen', 'url': '/helen'},
           {'name': 'Catherine', 'url': '/catherine'}]

@fellow_nav.route('/kristen')
def kristen():
    work_info =  [{
            'name': 'Summer Research Intern',
            'location': 'Western University',
            'start_date': 'May 2022',
            'end_date': 'Present',
            'desc': 'Developing recording GUI using python.'
        },{
            'name': 'Production Engineering Fellow',
            'location': 'MLH',
            'start_date': 'May 2022',
            'end_date': 'Present',
            'desc': 'Creating a portfolio website for orientation hack!'
        }]

    education_info = [{
            'name': 'Sir Frederick Banting S.S',
            'location': 'London, ON',
            'start_date': 'September 2016',
            'end_date': 'June 2020',
            'desc' : ''
        },{
            'name': 'Western University',
            'location': 'London, ON',
            'start_date': 'September 2020',
            'end_date': 'Present',
            'desc' : ''
        }]

    return render_template('kristen_page.html', title="22.SUM.22 Fellow: Kristen Zhang", url=os.getenv("URL"), work_info=work_info, education_info=education_info)

@fellow_nav.route('/helen')
def helen():
    work_info =  [{
            'name': 'Business Anaylst',
            'location': 'Scotiabank',
            'start_date': 'May 2022',
            'end_date': 'Present',
            'desc': 'Works with key stakeholders to align technology solutions with business strategies'
        },{
            'name': 'Production Engineering Fellow',
            'location': 'MLH',
            'start_date': 'May 2022',
            'end_date': 'Present',
            'desc': 'Production Engineering Fellowship hosted by MLH and Meta'
        },{
            'name': 'Software Engineer',
            'location': 'Scotiabank',
            'start_date': 'Sept 2021',
            'end_date': 'Dec 2021',
            'desc': 'Created regression models using Python and SQL to help price International ETFs'
        }]

    education_info = [{
            'name': 'University of Waterloo',
            'location': 'Waterloo, ON',
            'start_date': 'Sept 2020',
            'end_date': 'Present',
            'desc' : 'Bachelor of Computer Science Co-op'
        },{
            'name': 'Iroquois Ridge High School',
            'location': 'Oakville, ON',
            'start_date': 'Sept 2016',
            'end_date': 'June 2020',
            'desc' : 'Debate Club Marketing Executive, Interact Club Marketing Executive'
        }]
    

    return render_template('helen_page.html', nav=nav, title="Helen Xia", url=os.getenv("URL"), work_info=work_info, education_info=education_info)

@fellow_nav.route('/helen/hobbies')
def helenhobbies():
    hobby_info = [{
        'name' : 'Photography',
        'img' : '../static/img/helenhob1.png',
        'desc' : 'I like photographing my friends and people! I often like to adjust the picture through editing softwares. \
         the image above is a screenshot from my photography Instagram account (@hxlens).'
    },
    {
        'name' : 'Drawing',
        'img' : '../static/img/helenhob2.png',
        'desc' : 'I like drawing with different mediums. Like in forms of digitial art, paint, pencil and more.'
    }]

    return render_template('helen_hobbies.html', nav=nav, title="Helen Xia", url=os.getenv("URL"),hobbies=hobby_info)

@fellow_nav.route('/catherine')
def catherine():
    return "<p>Catherine<p>"