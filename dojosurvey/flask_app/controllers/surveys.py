from flask_app import app 
from flask import render_template, request, redirect, session, flash
from flask_app.models.survey import Survey

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validatesurvey', methods=['POST'])
def validate_survey():
    data = {
        'name':request.form['name'],
        'location':request.form['location'],
        'language':request.form['language'],
        'comment':request.form['comment']
    }
    if Survey.validate_survey(request.form):
        survey = Survey.save(data)
        return redirect('/results')
    else:
        return redirect('/')

@app.route('/results')
def results():
    return render_template('results.html')