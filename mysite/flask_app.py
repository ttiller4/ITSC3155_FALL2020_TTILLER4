# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for

app = Flask(__name__)

notes = {1: {'title': 'First Note', 'text': 'This is my first note', 'date': '10-1-2020'},
             2: {'title': 'Second Note', 'text': 'This is my second note', 'date': '10-2-2020'},
             3: {'title': 'Third Note', 'text': 'This is my third note', 'date': '10-3-2020'}
             }

@app.route('/index')
def index():
    a_user = {'name': 'Mogli', 'email':'mogli@uncc.edu'}

    return render_template('index.html', user = a_user)

@app.route('/notes')
def get_notes():

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

    if request.method == 'POST':
        title = request.form['title']
        text = request.form['noteText']
        from datetime import date
        today = date.today()
        today = today.strftime("%m-%d-%Y")
        id = len(notes)+1
        notes[id] = {'title': title, 'text':text, 'date':today}

        return redirect(url_for('get_notes', name = a_user))

    else:
        return render_template('new.html', user=a_user)




