from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CategoriesForm(FlaskForm):
    name = StringField("Kategoria", [validators.Length(min=5)])
<<<<<<< HEAD
    desc = StringField("Kategorian kuvaus")
=======
    desc = StringField("Kategorian kuvaus", [validators.Length(min=5)])
>>>>>>> 737aaca... muutoksia kirjautumiseen sekä layouttiin

    class Meta:
        csrf = False