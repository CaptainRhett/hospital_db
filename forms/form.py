from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, validators

class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirm Password')
    role = SelectField('Role', choices=[('医生', 'Doctor'), ('patient', 'Patient'), ('admin', 'Admin')])
    submit = SubmitField('Register')
