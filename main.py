import os
from flask import Flask, render_template, request
from application.database import db
from flask_restful import Api, Resource

current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(current_dir, 'QuantifiedSelfDB.sqlite3')

app.secret_key = "super secret key"

# db = SQLAlchemy()
db.init_app(app)
api = Api(app)
app.app_context().push()

from application.contollers import *
from application.api import LoggerAPI
api.add_resource(LoggerAPI, '/api/logger/', '/api/logger/<string:id>')

if __name__ == "__main__":
    app.run(debug=True)