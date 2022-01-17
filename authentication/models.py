import email
from unittest.util import _MAX_LENGTH
from authentication import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(length= 30), nullable = False, unique = True)
    email = db.Column(db.String(length= 100), nullable= False, unique = True)
    password = db.Column(db.String(length=60), nullable= False, unique  =True)


    def __str__(self):
        return self.username

