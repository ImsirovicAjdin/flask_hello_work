# start by adding a new db in bask: createdb hello_work
# mkdir hello_work && cd hello_work && touch flask_hello_work.py && code .

from flask import Flask # (1)
from flask_sqlalchemy import SQLAlchemy # (6)

app = Flask(__name__) # (2)

db = SQLAlchemy(app) # (7)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hello_work' # (8)

@app.route('/') # (3)
def index(): # (4)
    # (17) return "Hello work!" # (5)

    person = Person.query.first() # (17)
    return 'Hello ' + person.name # (17)

class Person(db.Model): # (9)
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>' # (16)

db.create_all() # (10)

# (11) Run the app with: FLASK_APP=flask_hello_work.py FLASK_DEBUG=true flask run
# (12) Run psql
# ```
# psql hello_work
# ```
# (13) Verify that the `persons` table exists
# ```
# \dt # shows the `persons` table is there
# ```
# (14) Verify the structure of the `persons` table
# ```
# \d persons # shows the structure of the `persons` table
# ```
# (15) Insert your name into the `persons` table
# ```
# INSERT INTO persons (name) VALUES ('Ajdin');
# ```
# (17) Fetch the newly added person in our `@app.route('/')`