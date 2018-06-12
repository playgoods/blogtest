from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, BooleanField)
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField("User Name", validators = [DataRequired(), Length(2,20) ])
    email = StringField("Email", validators = [DataRequired(), Email() ])
    password = PasswordField("Password", validators = [DataRequired(), Length(5,20)])
    confirm_password = PasswordField("Confrim Password", 
        validators = [DataRequired(),EqualTo('password')])
    submit = SubmitField("Sign Up")

class Login(FlaskForm):
    email = StringField("Email", validators = [DataRequired(), Email() ])
    password = PasswordField("Password", validators = [DataRequired(), Length(5,20)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")
