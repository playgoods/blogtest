from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, BooleanField)
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from blogtest.models import User

class RegistrationForm(FlaskForm):
    username = StringField("User Name", validators = [DataRequired(), Length(2,20) ])
    email = StringField("Email", validators = [DataRequired(), Email() ])
    password = PasswordField("Password", validators = [DataRequired(), Length(5,20)])
    confirm_password = PasswordField("Confrim Password", 
        validators = [DataRequired(),EqualTo('password')])
    submit = SubmitField("Sign Up")
    def validate_username(self,username):
        user= User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken. Plase Choese a different one. ")

    def validate_email(self,email):
        user= User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken. Plase Choese a different one. ")


class Login(FlaskForm):
    email = StringField("Email", validators = [DataRequired(), Email() ])
    password = PasswordField("Password", validators = [DataRequired(), Length(5,20)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")
