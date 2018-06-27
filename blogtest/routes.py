from flask import  render_template, url_for, flash, redirect, request
from blogtest.forms import RegistrationForm, Login, UpdateAccountForm
from blogtest import app, bcrypt, db
from blogtest.models import User,Post
from flask_login import login_user, current_user,logout_user,login_required

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
    if current_user.is_authenticated:
        return redirect(url_for("home"))
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
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
           login_user(user,remember=form.remember.data)
           next_page = request.args.get('next')
           return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Login unsuccessful. please check email and password","danger")
    return render_template("login.html",form=form, title = "Login" )

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account', methods=["POST","GET"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.valdiate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated!","success")
        return redirect(url_for("account"))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static',filename="profile_pics/"+ current_user.image_file)
    return render_template("account.html", title = "Account", image_file=image_file,form =form )
