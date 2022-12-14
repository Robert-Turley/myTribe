from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.user import User
from flask_app.models.tribe import Tribe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/tribes')
def display_tribes():
    if 'email' not in session:
        return redirect('/')
    return render_template('tribes.html')

#Displays tribe creation page
@app.route('/tribe/create')
def display_create_tribe():
    if 'email' not in session:
        return redirect('/')
    return render_template('create_tribe.html')

#Creates tribes after user submits form on creation_tribe.html
@app.route('/tribe/new', methods = ['POST'])
def create_tribe():
    #Validate, create then redirect to dashboard
    if Tribe.validate_tribe(request.form) == False:
        return redirect('/tribe/create')
    data = {
        **request.form,
        "user_id": session['user_id'],
    }
    Tribe.create(data)
    return render_template('tribe.html')

@app.route('/tribe/search')
def display_search_tribe():
    return render_template('search_tribe.html')