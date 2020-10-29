# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/notes')
def get_notes():

    notes = {1: {'title': 'First Note', 'text': 'This is my first note', 'date': '10-1-2020'},
             2: {'title': 'Second Note', 'text': 'This is my second note', 'date': '10-2-2020'}
             }

    return render_template('notes.html', notes=notes)




