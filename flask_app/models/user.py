from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import EMAIL_REGEX, DATABASE

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.user_name = data['user_name']
        self.email = data['email']
        self.password = data['password']
        self.cause1 = data['cause1']
        self.cause2 = data['cause2']
        self.cause3 = data['cause3']
        self.city = data['city']
        self.state = data['state']
        self.zip = data['zip']
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

    @classmethod
    def get_one_validate_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if len(result) > 0:
            current_user = cls(result[0])
            return current_user
        else:
            return None

    @classmethod
    def create(cls,data):
        query = "INSERT INTO users (first_name,last_name,user_name,email,password,cause1,cause2,cause3,city,state,zip) VALUES (%(first_name)s,%(last_name)s,%(user_name)s,%(email)s,%(password)s,%(cause1)s,%(cause2)s,%(cause3)s,%(city)s,%(state)s,%(zip)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result