from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import EMAIL_REGEX

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.user_name = data['user_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_registration(data):
        is_valid = True
        if len(data['first_name']) < 2:
            is_valid = False
            flash("First name must be at least two characters", "error_registration_first_name")
        if len(data['last_name']) < 2:
            is_valid = False
            flash("Last name must be at least two characters", "error_registration_last_name")
        if len(data['user_name']) < 2:
            is_valid = False
            flash("Username must be at least two characters", "error_registration_user_name")
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Invalid email address","error_registration_email")
        if len(data['password']) < 8:
            is_valid = False
            flash("Password must be at least eight characters", "error_registration_password")
        if data['password'] != data['confirm_password']:
            is_valid = False
            flash("Passwords do not match","error_registration_password_confirm")
        return is_valid