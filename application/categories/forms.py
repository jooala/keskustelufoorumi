from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CategoriesForm(FlaskForm):
    name = StringField("Kategoria", [validators.Length(min=5)])
    desc = StringField("Kategorian kuvaus")

    class Meta:
        csrf = False