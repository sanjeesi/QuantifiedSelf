import os
from flask import Flask, render_template, request
from application.database import db

current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(current_dir, 'QuantifiedSelfDB.sqlite3')
# db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

from application.contollers import *

if __name__ == "__main__":
    app.run(debug=True)