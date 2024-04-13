
from flask import Blueprint, render_template, redirect, request, flash, url_for

from .module import User,Note
from .module import db

from flask_login import login_user, logout_user, login_required, current_user

from werkzeug.security import generate_password_hash, check_password_hash



auth = Blueprint('auth', __name__) # blueprint setUp 


@auth.route('/login',methods=['GET','POST'])
def login():
    # request.form => [('email','tim@gmail.com'),('password','123456')]
    #data = request.form['email']

    if request.method == "POST":

        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:

            if check_password_hash(user.password, password):

                flash("Logged in Successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Inccorect password, try again", category="danger")
        else:
            flash("Email doesnt exist.",category="error")

    return render_template("login.html",user=current_user)


@auth.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    flash("You are successfully logout!",category='success')
    return redirect(url_for('views.index_page'))



@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():

    if request.method == "POST":

        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        # check if user alrady exist
        if user:
            flash("User with this email already exist.",category="error")

        # validation  
        elif len(email) < 4:
            flash('Email must be greater than three characters!', category="error")
        elif len(firstName) < 2:
            flash('First Name must be grater than one character!', category="error")
        elif password1 != password2:
            flash('Password dont match!', category="error")
        elif len(password1) < 7:
            flash('Password must be at least seven characters!', category="error")
        else:
            #add user to database 
            new_user = User(email=email,password=generate_password_hash(password1),first_name=firstName)

            db.session.add(new_user)
            db.session.commit()

            #login_user(user, remember=True)
            flash('Account created!', category="success")

            return redirect(url_for('views.home')) #view - modela, home - method 

    return render_template("sign_up.html",user=current_user)


# Silvia 1234567