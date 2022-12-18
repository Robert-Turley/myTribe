from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
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

    # @classmethod
    # def find_all():
    #     query = "SELECT * FROM tribes JOIN users ON users.tribe_id = tribes.id"

    # @classmethod
    # def get_all_tribes(cls):
    #     list_tribes = []
    #     query = "SELECT * FROM tribes JOIN users ON users.tribe_id = tribes.id;"
    #     results = connectToMySQL(DATABASE).query_db(query)
    #     for row in results:
    #         current_tribe = cls(row)
    #         user_data = {
    #             **row,
    #             "created_at": row['users.created_at'],
    #             "updated_at": row['users.updated_at'],
    #             "id": row['users.id']
    #         }
    #         current_user = User(user_data)
    #         current_tribe.user = current_user
    #         list_tribes.append(current_tribe)
    #     return list_tribes

    @classmethod
    def get_all_tribes(cls):
        # list_tribes = []
        print("Success")
        query = "SELECT * FROM tribes;"
        print("More success")
        results = connectToMySQL(DATABASE).query_db(query)
        # for row in results:
        #     current_tribe = cls(row)
        #     user_data = {
        #         **row,
        #         "created_at": row['users.created_at'],
        #         "updated_at": row['users.updated_at'],
        #         "id": row['users.id']
        #     }
        #     current_user = User(user_data)
        #     current_tribe.user = current_user
        # list_tribes.append(results)
        print("Even more success")
        print(results)
        return results

    @classmethod
    def get_all_with_users(cls):
        query = "SELECT * FROM tribes JOIN users ON users.tribe_id = tribes.id;"
        result = connectToMySQL(DATABASE).query_db(query)
        list_tribes = []
        for row in result:
            current_tribe = cls(row)

    # @classmethod
    # def get_users_for_tribe(cls,data):
    #     query = "SELECT * FROM tribes LEFT JOIN users ON tribes.id = users.tribe_id WHERE tribes.id = %(id)s;"
    #     result = connectToMySQL(DATABASE).query_db(query,data)
    #     tribe_info = cls(result[0])
    #     for row in result:
    #         r = {
    #             "id": row['ninjas.id'],
    #             "first_name": row['first_name'],
    #             "last_name": row['last_name'],
    #             "age": row['age'],
    #             "created_at": row['created_at'],
    #             "updated_at": row['updated_at'],
    #         }
    #         tribe_info.users.append(User(r))
    #     return tribe_info
    
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