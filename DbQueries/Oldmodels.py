import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, Boolean, Float
from sqlalchemy import select

from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Tracker(Base):
    __tablename__ = 'Tracker'
    id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    trackerType = Column(String)
    settings = Column(String)
    # log = relationship("Log")

class Log(Base):
    __tablename__ = 'Log'
    timeStamp = Column(DateTime)
    trackerId = Column(String, ForeignKey('Tracker.id'))
    value = Column(String)
    note = Column(String)

engine = create_engine("sqlite:///./QuantifiedSelfDB.sqlite3")

if __name__ == '__main__':
    with Session(engine, autoflush=False) as session:
        session.begin()
        try:
            pass
        except:
            print("Exception, rolling back")
            session.rollback()
            raise
        else:
            print("No exception, committing")
            session.commit()