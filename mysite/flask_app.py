# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from database import db
from models import Note as Note
from models import User as User
from forms import RegisterForm
from flask import session
from flask_bcrypt import bcrypt
from forms import LoginForm

# from flask_app import app as application

app = Flask(__name__)

#notes = {1: {'title': 'First Note', 'text': 'This is my first note', 'date': '10-1-2020'},
      #       2: {'title': 'Second Note', 'text': 'This is my second note', 'date': '10-2-2020'},
       #      3: {'title': 'Third Note', 'text': 'This is my third note', 'date': '10-3-2020'}
        #     }





app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://troytillery:2020hellcaT!@troytillery.mysql.pythonanywhere-services.com/troytillery$default'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY'] = 'SE3155'
#  Bind SQLAlchemy db object to this Flask app
db.init_app(app)

# Setup models
with app.app_context():
    db.create_all()   # run under the app context



@app.route('/')
@app.route('/index')
def index():

    if session.get('user'):
        return render_template("index.html", user=session['user'])
    return render_template("index.html")

@app.route('/notes')
def get_notes():

    if session.get('user'):
       # a_user = db.session.query(User).filter_by(email='ttiller4@uncc.edu').one()
        my_notes = db.session.query(Note).filter_by(user_id=session['user_id']).all()

        return render_template('notes.html', notes=my_notes, user=session['user'])
    else:
        return redirect(url_for('login'))

@app.route('/notes/<note_id>')
def get_note(note_id):

    #a_user = db.session.query(User).filter_by(email='ttiller4@uncc.edu').one()
    my_note = db.session.query(Note).filter_by(id=note_id)

    return render_template('note.html', note=my_note)

@app.route('/notes/new', methods=['GET', 'POST'])
def new_note():
    #a_user = {'name': 'Troy', 'email': 'ttiller4@uncc.edu'}

    if session.get('user'):
        if request.method == 'POST':
            title = request.form['title']
            text = request.form['noteText']
            from datetime import date
            today = date.today()
            today = today.strftime("%m-%d-%Y")
            new_record = Note(title, text, today, session['user_id'])
            db.session.add(new_record)
            db.session.commit()

            return redirect(url_for('get_notes'))

        else:
             return render_template('new.html', user=session['user'])

        #a_user = db.session.query(User).filter_by(email='ttiller4@uncc.edu').one()
    else:
        return redirect(url_for('login'))
@app.route('/notes/edit/<note_id>')
def update_note(note_id):

    if session.get('user'):
        if request.method == 'POST':
            title = request.form['title']
            text = request.form['noteText']
            note = db.session.query(Note).filter_by(id=note_id).one()
            note.title = title
            note.text = text
            db.session.add(note)
            db.session.commit()

            return redirect(url_for('get_notes'))

        else:

            #a_user = db.session.query(User).filter_by(email='mogli@uncc.edu').one()
            my_note = db.session.query(Note).filter_by(id=note_id).one()
            return render_template('new.html', note=my_note, user=session['user'])
    else:
        return redirect(url_for('login'))

@app.route('/notes/delete/<note_id>', methods=['POST'])
def delete_note(note_id):

    if session.get('user'):

       my_note = db.session.query(Note).filter_by(id=note_id).one()
       db.session.delete(my_note)
       db.session.commit()

       return redirect(url_for('get_notes'))
    else:
        return redirect(url_for('login'))

@app.route('/register', methods=['POST','GET'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        password_hash = bcrypt.hashpw(
            request.form['password'].encode('utf-8'), bcrypt.gensalt())
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        new_record = User(first_name, last_name, request.form['email'], password_hash)
        db.session.add(new_record)
        db.session.commit()
        session['user'] = first_name
        the_user = db.session.query(User).filter_by(email=request.form['email']).one()
        session['user_id'] = the_user.id

        return redirect(url_for('get_notes'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    # validate_on_submit only validates using POST
    if login_form.validate_on_submit():
        # we know user exists. We can use one()
        the_user = db.session.query(User).filter_by(email=request.form['email']).one()
        # user exists check password entered matches stored password
        if bcrypt.checkpw(request.form['password'].encode('utf-8'), the_user.password):
            # password match add user info to session
            session['user'] = the_user.first_name
            session['user_id'] = the_user.id
            # render view
            return redirect(url_for('get_notes'))

        # password check failed
        # set error message to alert user
        login_form.password.errors = ["Incorrect username or password."]
        return render_template("login.html", form=login_form)
    else:
        # form did not validate or GET request
        return render_template("login.html", form=login_form)


