from flask_wtf import FlaskForm
from wtforms import StringField, validators


class TopicsForm(FlaskForm):
    name = StringField("Aiheen otsikko", [validators.Length(min=5)])
    desc = StringField("Aiheen kuvaus")

    class Meta:
        csrf = False