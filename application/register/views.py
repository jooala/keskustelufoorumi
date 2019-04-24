from flask import redirect, render_template, request, url_for, flash
from application.register.forms import RegisterForm
from application import app, db
from application.auth.models import User


@app.route("/register")
def register_form():
    return render_template("register/register.html", form = RegisterForm())

@app.route("/register/", methods=["GET", "POST"])
def register_create():
    form = RegisterForm(request.form)
    if not form.validate():
        return render_template("register/register.html", form = RegisterForm(), error = "Nimi ja käyttäjätunnus pitää olla yli 3 kirjainta ja salasana 5 kirjainta pitkä vähintään.")

    

    query = "SELECT * FROM account WHERE username = :username"
    if db.session().execute(query, {'username': form.username.data}).first():
        return render_template("register/register.html", form = RegisterForm(), error = "Username already exists")
    else:

        t = User(form.name.data, form.username.data, form.password.data, "USER")
  
        db.session().add(t)
        db.session().commit()
  
    return redirect(url_for("auth_login"))