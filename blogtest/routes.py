from flask import  render_template, url_for, flash, redirect
from blogtest.forms import RegistrationForm, Login
from blogtest import app, bcrypt, db
from blogtest.models import User,Post
from flask_login import login_user

posts = [
        {
            "author": "Mohamed Ali",
            "title" : " the first blog",
            "content" : " the test fake date for first blog ",
            "date_posted" : "2018-05-16 19:10"
        },
        {
            "author": "Mohamed Ali",
            "title" : " the second blog",
            "content" : " the test fake date for second blog ",
            "date_posted" : "2018-05-16 20:00"
        }
        ]

@app.route('/home')
@app.route('/')
def home():
    return render_template("home.html",posts=posts)


@app.route('/about')
def about():
    return render_template("about.html", title=" the about blask ")

@app.route('/register', methods=["POST","GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,password=hashed_password,email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash("your account has been created! you are now able to login", "success")
        return redirect(url_for('login'))
    return render_template("register.html",form=form, title = "Register" )

@app.route('/login', methods=["POST","GET"])
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
           login_user(user,remember=form.remember.data)
           return redirect(url_for('home'))
        else:
            flash("Login unsuccessful. please check email and password","danger")
    return render_template("login.html",form=form, title = "Login" )
