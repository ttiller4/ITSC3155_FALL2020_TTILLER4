# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from database import db
from models import Note as Note
from models import User as User
#from flask_app import app as application

app = Flask(__name__)

#notes = {1: {'title': 'First Note', 'text': 'This is my first note', 'date': '10-1-2020'},
      #       2: {'title': 'Second Note', 'text': 'This is my second note', 'date': '10-2-2020'},
       #      3: {'title': 'Third Note', 'text': 'This is my third note', 'date': '10-3-2020'}
        #     }





app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://troytillery:2020hellcaT!@troytillery.mysql.pythonanywhere-services.com/troytillery$default'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
#  Bind SQLAlchemy db object to this Flask app
db.init_app(app)

# Setup models
with app.app_context():
    db.create_all()   # run under the app context



@app.route('/')
@app.route('/index')
def index():
    a_user = db.session.query(User).filter_by(email='ttiller4@uncc.edu').one()

    return render_template('index.html', user = a_user)

@app.route('/notes')
def get_notes():
        a_user = db.session.query(User).filter_by(email='ttiller4@uncc.edu').one()
        my_notes = db.session.query(Note).all()

        return render_template('notes.html', notes=my_notes, user=a_user)

@app.route('/notes/<note_id>')
def get_note(note_id):

 #   a_user = db.session.query(User).filter_by(email='ttiller4@uncc.edu').one()
    my_note = db.session.query(Note).filter_by(id=note_id)

    return render_template('note.html', note=my_note)

@app.route('/notes/new', methods=['GET', 'POST'])
def new_note():
    a_user = {'name': 'Troy', 'email': 'ttiller4@uncc.edu'}

    if request.method == 'POST':
        title = request.form['title']
        text = request.form['noteText']
        from datetime import date
        today = date.today()
        today = today.strftime("%m-%d-%Y")
        newEntry = Note(title, text, today)
        db.session.add(newEntry)
        db.session.commit()

        return redirect(url_for('get_notes', name = a_user))

    else:

        a_user = db.session.query(User).filter_by(email='ttiller4@uncc.edu').one()

        return render_template('new.html', user=a_user)

@app.route('/notes/edit/<note_id>')
def update_note(note_id):

    a_user = db.session.query(User).filter_by(email='mogli@uncc.edu').one()
    my_note = db.session.query(Note).filter_by(id=note_id).one()
    return render_template('new.html', note=my_note, user=a_user)


