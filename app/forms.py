from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BoolenField, SubmitField
from wtforms.validators import DataRequest


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequest()])
    password = PasswordField('Passwrod', validators=[DataRequest()])
    remember_me = BoolenField('Remember Me')
    submit = SubmitField('Sing in')