import re
from flask_restful import Resource
from application.database import db
from application.models import Tracker, Log

class LoggerAPI(Resource):
    def get(self, id):
        return {"hello": db.session.query(Tracker).filter_by(id=id).first().name}, 200

    def post(self):
        req = request.get_json()
        print("req:", req)
        # log = Log(trackerId=trackerId, timeStamp=timestamp, value=value, note=note)
        # print("logged", log)
        # db.session.add(log)
        # db.session.commit()
        print("Log added successfully!")
        return "", 201