from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW())"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)
    
    @staticmethod
    def validate_survey(survey):
        is_valid = True
        #change the number (1) if you want more than one character 
        print(survey['location'])
        if len(survey['name']) < 1: 
            flash('We need your name')
            is_valid = False 
        if survey['location'] == 'Select Location':
            flash('We need your location')
            is_valid = False
        if survey['language'] == 'Select Language':
            flash('We need your favorite language')
            is_valid = False
        return is_valid