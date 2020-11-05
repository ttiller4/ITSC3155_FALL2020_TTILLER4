# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/index')
def index():
    a_user = {'name': 'Mogli', 'email':'mogli@uncc.edu'}

    return render_template('index.html', user = a_user)

@app.route('/notes')
def get_notes():
        notes = {1: {'title': 'First Note', 'text': 'This is my first note', 'date': '10-1-2020'},
             2: {'title': 'Second Note', 'text': 'This is my second note', 'date': '10-2-2020'},
             3: {'title': 'Third Note', 'text': 'This is my third note', 'date': '10-3-2020'}
             }
        return render_template('notes.html', notes=notes)

@app.route('/notes/<note_id>')
def get_note(note_id):

    notes = {1: {'title': 'First Note', 'text': 'This is my first note', 'date': '10-1-2020'},
             2: {'title': 'Second Note', 'text': 'This is my second note', 'date': '10-2-2020'},
             3: {'title': 'Third Note', 'text': 'This is my third note', 'date': '10-3-2020'}
             }

    return render_template('note.html', note=notes[int(note_id)])

@app.route('/notes/new', methods=['GET', 'POST'])
def new_note():
    a_user = {'name': 'Mogli', 'email': 'mogli@uncc.edu'}

    print('request method is', request.method)
    if request.method == 'POST':
        request_data = request.form
        return f"data: {request_data} !"
    else:
        return render_template('new.html', user=a_user)




