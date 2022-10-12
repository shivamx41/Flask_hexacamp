from sqlite3 import dbapi2
from xml.dom.expatbuilder import ParseEscape
from flask import Flask, render_template, url_for, redirect, request, flash
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String,ForeignKey,asc,desc
from sqlalchemy.sql import select



app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

engine = create_engine('mysql://root:brainbeam@localhost/hexahealth', echo = True)
meta = MetaData()

users = Table(
   'users', meta, 
   Column('id', Integer, primary_key = True), 
   Column('firstname', String(50)), 
   Column('lastname', String(50)),
   Column('email', String(100)),
   Column('username', String(100)),
   Column("password", String(100))
)


camp_ground = Table(
   'camp_ground', meta, 
   Column('camp_id', Integer, primary_key=True),
   Column('id', Integer,ForeignKey('users.id')),
   Column('Title', String(100)),
   Column('Description', String(2000)),
   Column('Price', Integer),
   Column('Images', String(100)),
   Column('Email', String(100)),
   Column('Mobile', Integer),
   Column('Location', String(100)),
   Column('Latitude', String(100)),
   Column('longitude', String(100))  

)


reviews = Table(
   'reviews', meta, 
   Column('review_id', Integer, primary_key=True),
   Column('id', Integer,ForeignKey('users.id')),
   Column('review_rating', Integer),
   Column('review_description', String(2000))

)


# meta.create_all(engine)

conn = engine.connect()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.get('/productdashboard')
def productdashboard():
    # return render_template('productdashboard.html')
    return 'log in sucessfull'

@app.get('/login')
def login():
    # print(url_for('login'))
    return render_template('login.html')


@app.get('/signup')
def signup():
    # print(url_for('login'))
    return render_template('signup.html')

@app.post('/logout')
def logout():
    pass

@app.post('/register')
def register():
    newuser = request.form
    print(newuser)
    stmt = users.insert().values(newuser)
    result = conn.execute(stmt)
    return redirect(url_for('login'))

@app.patch('/changepassword')
def change_password():
    pass

@app.patch('/updateprofile')
def update_profile():
    pass

@app.post('/authenticate')
def authenticate():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('productdashboard'))
    return render_template('login.html', error=error)

if(__name__=='__main__'):
    app.run(debug=True)
    
    