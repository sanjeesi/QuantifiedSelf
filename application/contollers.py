from sqlite3 import Timestamp
from flask import Flask, render_template, request
from flask import redirect, url_for
from flask import current_app as app
from flask import flash
from application.models import Tracker, Log
import datetime
from .database import db
import requests
import sqlite3

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        return redirect('/tracker/' + username)
    else:
        print("Something went wrong. Error Check!")

@app.route('/tracker/<username>', methods=['GET', 'POST'])
def tracker(username):
    # trackers = Tracker.query.all()
    trackers = db.session.query(Tracker).all()
    return render_template('trackers.html', trackers=trackers, username= username)

@app.route('/log/<trackerId>,<username>', methods=['GET', 'POST'])
def log(trackerId,username):
    #display logs index page
    logs = Log.query.filter_by(trackerId=trackerId).all()
    # print("print:", logs.trackerId)
    return render_template('logs.html', logs=logs, tracker = Tracker.query.filter_by(id=trackerId).first().name, username=username)

@app.route('/addLog/<trackerId>,<username>', methods=['GET', 'POST'])
def addLog(trackerId, username):
    if request.method == 'GET':
        timestamp = datetime.datetime.now()
        # print("timestamp:", timestamp)
        return render_template('addLog.html', username=username, tracker=Tracker.query.filter_by(id=trackerId).first().name, timestamp=timestamp.strftime("%Y-%m-%dT%H:%M:%S"))
    elif request.method == 'POST':
        timestamp = request.form['when']
        value = request.form['value']
        note = request.form['note']
        log = Log(trackerId=trackerId, timeStamp=timestamp, value=value, note=note)
        db.session.add(log)
        db.session.commit()
        print("Log added successfully!")
        # print("calling insertLog")
        # # res = requests.post('http://127.0.0.1:5000/api/logger', json={"mytext":"lalala"})
        # insertLog(trackerId, timestamp, value, note)
        flash('Event logged successfully!')
        return redirect('/tracker/' + username)
    else:
        print("Something went wrong. Error Check!")

@app.route('/editLog/<timestamp>,<username>', methods=['GET', 'POST'])
def editLog(timestamp, username):
    log = Log.query.filter_by(timeStamp=timestamp).first()
    if request.method == 'GET':
        return render_template('editLog.html', username=username, tracker=Tracker.query.filter_by(id=log.trackerId).first().name, log=log)
    elif request.method == 'POST':
        log.timeStamp=request.form['when']
        log.value=request.form['value']
        log.note=request.form['note']
        db.session.add(log)
        db.session.commit()
        flash('Event edited successfully!')
        return redirect('/tracker/' + username)

@app.route('/deleteLog/<timestamp>,<username>')
def deleteLog(timestamp, username):
    log = Log.query.filter_by(timeStamp=timestamp).first()
    db.session.delete(log)
    db.session.commit()
    return redirect('/tracker/' + username)