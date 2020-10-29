# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index')
def hello_world():

    a_user = {'name': 'Troy Tillery', 'email':'ttiller4@uncc.edu'}

    return render_template("index.html", user = a_user)




