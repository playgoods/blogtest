from flask import Flask , render_template, url_for

app = Flask(__name__)

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
def index():
    return render_template("home.html",posts=posts)

@app.route('/about')
def about():

    return render_template("about.html", title=" the about blask ")

