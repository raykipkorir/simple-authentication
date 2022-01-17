from authentication import app
from flask import render_template, url_for, redirect,flash

from authentication.forms import Loginform, Registerform
from authentication.models import User
from authentication import db
@app.route("/")
def login():
    form = Loginform()
    return render_template('login.html', form = form)

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = Registerform()
    if form.validate_on_submit():
        new_data = User(username = form.username.data, email = form.email.data, password = form.password1.data)
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('register.html', form = form)

