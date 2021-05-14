# start by adding a new db in bask: createdb hello_work
# mkdir hello_work && cd hello_work && touch flask_hello_work.py && code .

from flask import Flask # (1)
from flask_sqlalchemy import SQLAlchemy # (6)

app = Flask(__name__) # (2)

db = SQLAlchemy(app) # (7)

@app.route('/') # (3)
def index(): # (4)
    return "Hello work!" # (5)