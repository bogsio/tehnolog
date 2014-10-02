from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email


class LoginForm(Form):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])


class PostForm(Form):
    title = StringField('title', validators=[DataRequired()])
    content = TextAreaField('content', validators=[DataRequired()])
    summary = TextAreaField('summary', validators=[DataRequired()])


class CategoryForm(Form):
    category_name = StringField('category_name', validators=[DataRequired()])