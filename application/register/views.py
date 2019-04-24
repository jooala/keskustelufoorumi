from flask import redirect, render_template, request, url_for
from application.register.forms import RegisterForm
from application import app, db
from application.auth.models import User


@app.route("/register")
def register_form():
    return render_template("register/register.html", form = RegisterForm())

@app.route("/register/", methods=["POST"])
def register_create():
    form = RegisterForm(request.form)
    if not form.validate():
        return render_template("register/register.html", form = form)
    t = User(form.name.data, form.username.data, form.password.data, "USER")
  
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("categories_index"))