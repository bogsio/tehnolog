import flask
from flask import request
from app import app
from themes import ThemeManager
from app.models import User
from app.forms import LoginForm
from app.manager import ModelManager

Theme = ThemeManager.get_theme(app.config['THEME'])

@app.route('/admin/')
def admin_index():
    user = User.get_current_user()
    if user is None:
        return flask.redirect(flask.url_for('admin_login'))



    return flask.render_template(Theme.get_template(page='admin_index'),
                                 manager=ModelManager)


@app.route('/login/', methods=['GET', 'POST'])
def admin_login():
    user = User.get_current_user()
    if user is not None:
        return flask.redirect(flask.url_for('admin_index'))

    login_form = LoginForm()

    if request.method == 'POST' and login_form.validate_on_submit():
        # Actually check if we have such a user in the db
        existing_user, error = User.authenticate(login_form.email.data,
                                                 login_form.password.data)

        if existing_user:
            existing_user.login()
            return flask.redirect(flask.url_for('admin_index'))

        login_form.email.errors.append('Invalid username or password')

    return flask.render_template(Theme.get_template(page='admin_login'),
                                 manager=ModelManager, form=login_form)


@app.route('/logout/', methods=['GET', 'POST'])
def admin_logout():
    User.logout()
    return flask.redirect(flask.url_for('admin_login'))


@app.route('/post/add/', methods=['GET', 'POST'])
def admin_add_post():
    return flask.render_template(Theme.get_template(page='admin_add_post'),
                                 manager=ModelManager)

