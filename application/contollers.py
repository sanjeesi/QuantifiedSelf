from flask import Flask, render_template, request
from flask import redirect, url_for
from flask import current_app as app
from application.models import Tracker, Log

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
    trackers = Tracker.query.all()
    return render_template('trackers.html', trackers=trackers, username= username)

@app.route('/log/<trackerId>', methods=['GET', 'POST'])
def log(trackerId):
    #display logs index page
    pass

