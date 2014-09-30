import flask
from flask import request
from app import app, db
from themes import ThemeManager
from app.models import User, Post
from app.forms import LoginForm, PostForm
from app.manager import ModelManager

Theme = ThemeManager.get_theme(app.config['THEME'])

@app.route('/admin/')
def admin_index():
    user = User.get_current_user()
    if user is None:
        return flask.redirect(flask.url_for('admin_login'))



    return flask.render_template(Theme.get_template(page='admin_index'),
                                 manager=ModelManager)


@app.route('/admin/login/', methods=['GET', 'POST'])
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


@app.route('/admin/logout/', methods=['GET', 'POST'])
def admin_logout():
    User.logout()
    return flask.redirect(flask.url_for('admin_login'))


@app.route('/admin/post/add/', methods=['GET', 'POST'])
def admin_add_post():
    form = PostForm()

    if request.method == 'POST' and form.validate_on_submit():
        post = Post(title=request.form['title'],
                    content=request.form['content'],
                    summary=request.form['summary'])
        db.session.add(post)
        db.session.commit()
        db.session.flush()
        flask.flash('Your post has been created', 'success')

    return flask.render_template(Theme.get_template(page='admin_add_post'),
                                 manager=ModelManager,
                                 post_form=form)

@app.route('/admin/post/<id>/', methods=['GET', 'POST'])
def admin_detail_post(id):
    return flask.render_template(Theme.get_template(page='admin_detail_post'),
                                 manager=ModelManager,
                                 post_id=id)
