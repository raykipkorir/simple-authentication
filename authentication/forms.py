from cProfile import label
import email
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class Registerform(FlaskForm):
    username = StringField(label = 'Username: ')
    email = StringField(label= 'Email Address:')
    password1 = StringField(label = 'Enter Password:')
    password2 = StringField(label  ='Confirm Password:')
    submit = SubmitField(label = 'Create Account')


class Loginform(FlaskForm):
    username = StringField(label = "Username:")
    password = StringField(label='Enter Password:')
    submit = SubmitField(label="Log In")