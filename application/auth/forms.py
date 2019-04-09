from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
<<<<<<< HEAD


class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")

=======
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
>>>>>>> 737aaca... muutoksia kirjautumiseen sekä layouttiin
    class Meta:
        csrf = False
