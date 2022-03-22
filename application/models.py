from .database import db

class Tracker(db.Model):
    __tablename__ = 'tracker'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    trackerType = db.Column(db.String)
    settings = db.Column(db.String)
    # log = relationship("Log")

class Log(db.Model):
    __tablename__ = 'logs'
    timeStamp = db.Column(db.String, primary_key=True)
    trackerId = db.Column(db.String, db.ForeignKey('Tracker.id'))
    value = db.Column(db.String)
    note = db.Column(db.String)