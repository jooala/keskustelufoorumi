from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CategoriesForm(FlaskForm):
    name = StringField("Kategoria", [validators.Length(min=4, max=50)])
    desc = StringField("Kategorian kuvaus", [validators.Length(max=50)])

    class Meta:
        csrf = False