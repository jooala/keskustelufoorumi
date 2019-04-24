from flask_wtf import FlaskForm
from wtforms import StringField, validators


class TopicsForm(FlaskForm):
    name = StringField("Aiheen otsikko", [validators.Length(min=5, max=255)])
    desc = StringField("Aiheen kuvaus", [validators.Length(min=5, max=255)])

    class Meta:
        csrf = False