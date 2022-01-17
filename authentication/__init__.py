from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a5583a03fe5cfe981bfda5b3'

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///core.db'
db = SQLAlchemy(app)

from authentication import routes