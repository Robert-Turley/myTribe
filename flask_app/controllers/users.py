from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import User

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/user/create', methods = ['POST'])
def registration():
    # Validate registration
    if User.validate_registration(request.form) == False:
        return redirect('/')
    # Connect to model

    # Validate if user exists, if not create