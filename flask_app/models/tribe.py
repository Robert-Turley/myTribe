from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import EMAIL_REGEX, DATABASE

class Tribe:
    all_tribes = []
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = "Ohio"
        self.cause = data['cause']
        self.funds = data['funds']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        Tribe.all_tribes.append(self)