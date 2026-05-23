from flask import Flask
from flask import main
app = Flask(__name__)

import flaskr.main

from flaskr import db
db.create_books_table()
