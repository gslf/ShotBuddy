from flask import render_template, redirect, url_for
from flask_login import current_user, login_user, login_required, logout_user
from webapp.forms.LoginForm import LoginForm
from webapp import app
from webapp.User import User
from webapp.UsersManager import UsersManager

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        users_manager = UsersManager(user)

        if users_manager.check():
            rememberMe = form.remember_me.data

            if login_user(user, rememberMe):
                login_user(user, rememberMe)
                return redirect(url_for('dashboard'))

            else:
                #TODO ERROR
                return redirect(url_for('index'))

    return render_template('home.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))

    return render_template('dashboard.html')

@app.route('/session')
@login_required
def session():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))

    return render_template('session.html')


@app.route('/history')
@login_required
def history():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))

    return render_template('history.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
