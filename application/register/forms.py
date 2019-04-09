from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField


class RegisterForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=3)])
    username = StringField("Käyttäjätunnus", [validators.Length(min=3)])
    password = PasswordField("Salasana")

    class Meta:
        csrf = False