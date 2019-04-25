from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ProfilesForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=4, max=50)])

    class Meta:
        csrf = False