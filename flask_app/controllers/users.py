from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/user/create', methods = ['POST'])
def registration():
    # Validate registration
    if User.validate_registration(request.form) == False:
        return redirect('/')
    # Validate if user exists, if not create
    current_user = User.get_one_validate_email(request.form)
    if current_user != None:
        flash("Email already exists!","error_registration_email")
        return redirect ('/')
    data = {
        **request.form,
        # "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    print(data)
    user_id = User.create(data)

    session['first_name'] = data['first_name']
    session['email'] = data['email']
    session['user_id'] = user_id

    return redirect('/profile')

@app.route('/user/login', methods = ['POST'])
def process_login():
    current_user = User.get_one_validate_email(request.form)
    if current_user != None:
        if not bcrypt.check_password_hash(current_user.password,request.form['password']):
            flash("Passord is invalid","error_login_password")
            return redirect('/')
        session['first_name'] = current_user.first_name
        session['email'] = current_user.email
        session['user_id'] = current_user.id
        return redirect('/dashboard')
    else:
        flash("Password is invalid","error_login_password")
        return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        return redirect ('/')
    return render_template('dashboard.html')

@app.route('/create/profile')
def create_profile():
    return render_template('profile.html')