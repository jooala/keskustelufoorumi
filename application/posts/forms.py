from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators

class PostsForm(FlaskForm):
    message = TextAreaField("Viesti", [validators.length(min=3)])

    class Meta:
        csrf = False