from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.categories.models import Categories
from application.categories.forms import CategoriesForm





@app.route("/categories", methods=["GET"])
@login_required(role="ADMIN")
def categories_index():
    return render_template("categories/list.html", categories = Categories.query.all())

@app.route("/categories/new/")
@login_required(role="ADMIN")
def categories_form():
    return render_template("categories/new.html", form=CategoriesForm())
  

@app.route("/categories/<category_id>/", methods=["POST"])
@login_required(role="ADMIN")
def categories_set_text(category_id):
    form = CategoriesForm(request.form)
    if not form.validate():
        return render_template("categories/list.html", categories = Categories.query.all())
    t = Categories.query.get(category_id)
    t.name = request.form.get("name")
    t.desc = request.form.get("desc")
    db.session().commit()

    return redirect(url_for("categories_index"))

@app.route("/categories/<category_id>/", methods=["POST"])
@login_required(role="ADMIN")
def categories_set_desc(category_id):
    form = CategoriesForm(request.form)
    if not form.validate():
        return render_template("categories/list.html", categories = Categories.query.all())
    t = Categories.query.get(category_id)
    t.desc = request.form.get("desc")
    db.session().commit()

    return redirect(url_for("categories_index"))

@app.route("/categories/<category_id>/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def categories_delete(category_id):
    t = Categories.query.get(category_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("categories_index"))


@app.route("/categories/", methods=["POST"])
@login_required(role="ADMIN")
def categories_create():
    form = CategoriesForm(request.form)
    if not form.validate():
        return render_template("categories/new.html", form=form)
    t = Categories(form.name.data, form.desc.data)
  
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("categories_index"))
