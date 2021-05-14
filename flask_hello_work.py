# start by adding a new db in bask: createdb hello_work
# mkdir hello_work && cd hello_work && touch flask_hello_work.py && code .

from flask import Flask # (1)

app = Flask(__name__) # (2)

@app.route('/') # (3)