import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', title="MLH Fellow Orientation Hack", url=os.getenv("URL"))
