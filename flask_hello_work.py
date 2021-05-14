# start by adding a new db in bask: createdb hello_work
# mkdir hello_work && cd hello_work && touch flask_hello_work.py && code .

from flask import Flask # (1)
from flask_sqlalchemy import SQLAlchemy # (6)

app = Flask(__name__) # (2)

db = SQLAlchemy(app) # (7)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hello_work' # (8)

@app.route('/') # (3)
def index(): # (4)
    return "Hello work!" # (5)

class Person(db.Model): # (9)
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

db.create_all() # (10)

# (11) Run the app with: FLASK_APP=flask_hello_work.py FLASK_DEBUG=true flask run
