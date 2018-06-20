from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from  flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '72a23248a0ebcf2bfda6d42f7f080a90'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)

from blogtest import routes

