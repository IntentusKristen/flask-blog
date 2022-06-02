import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
from .fellow_nav import fellow_nav
app.register_blueprint(fellow_nav, url_prefix='/')


@app.route('/')
def home():
    return render_template('home.html', title="MLH Fellow Orientation Hack", url=os.getenv("URL"))
