from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField
from wtforms.validators import InputRequired


class RegisterForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=3,max=40), InputRequired()])
    username = StringField("Käyttäjätunnus", [validators.Length(min=3, max=30), InputRequired()])
    password = PasswordField("Salasana", [validators.Length(min=5, max=30), InputRequired()])

    class Meta:
        csrf = False