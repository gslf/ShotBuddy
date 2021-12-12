from flask import render_template
from webapp.forms.LoginForm import LoginForm
from webapp import app

@app.route('/')
@app.route('/index')
def index():
    form = LoginForm()
    return render_template('home.html', form=form)