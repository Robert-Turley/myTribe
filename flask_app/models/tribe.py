from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import EMAIL_REGEX, DATABASE

class Tribe:
    all_tribes = []
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = ['location']
        self.cause = data['cause']
        self.funds = data['funds']
        # self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        Tribe.all_tribes.append(self)

    @classmethod
    def create(cls,data):
        query = "INSERT INTO tribes (name,location,cause,funds) VALUES (%(name)s,%(location)s,%(cause)s,%(funds)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    @staticmethod
    def validate_tribe(data):
        is_valid = True
        if data['name'] == "":
            flash("Name cannot be empty", "error_tribe_name")
            is_valid = False
        if data['location'] == "":
            flash("Location cannot be empty", "error_tribe_location")
            is_valid = False
        if data['cause'] == "":
            flash("Cause cannot be empty", "error_tribe_cause")
            is_valid = False
        if data['funds'] == "":
            flash("Funds must be greater than 0", "error_tribe_funds")
            is_valid = False
        if len(data['name']) < 3:
            flash("Name cannot be less than 3 characters", "error_tribe_name")
            is_valid = False
        if len(data['location']) < 3:
            flash("Location cannot be less than 3 characters", "error_tribe_location")
            is_valid = False
        if len(data['cause']) < 3:
            flash("Cause cannot be less than 3 characters", "error_tribe_cause")
            is_valid = False
        return is_valid