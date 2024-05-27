from flask_app.config.mysqlconnection import connectToMySQL
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

DB = 'group_project'

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.repairs = []

    @staticmethod
    def validate(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DB).query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.", "danger")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email", "danger")
            is_valid=False
        if len(user['first_name']) < 3:
            flash("First name needs to be 3 characters or more.", "danger")
            is_valid= False
        if len(user['last_name']) < 3:
            flash("Last name needs to be 3 characters or more.", "danger")
            is_valid= False
        if len(user['password']) < 8:
            flash("Password needs to be 8 characters or more.", "danger")
            is_valid= False
        if user['password'] != user['confirm_pw']:
            flash("Passwords don't match.", "danger")
        return is_valid


    @classmethod
    def save(cls,data):
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());'
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_with_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DB).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])