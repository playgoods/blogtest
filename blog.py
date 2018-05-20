from flask import Flask , render_template, url_for, flash, redirect
from forms import RegistrationForm, Login

app = Flask(__name__)
app.config['SECRET_KEY'] = '72a23248a0ebcf2bfda6d42f7f080a90'

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
        flash(f"Account Created {form.username.data}","success")
        return redirect(url_for('home'))
    return render_template("register.html",form=form, title = "Register" )

@app.route('/login', methods=["POST","GET"])
def login():
    form = Login()
    return render_template("login.html",form=form, title = "Login" )
