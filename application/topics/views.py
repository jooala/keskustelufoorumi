from application import app, db
from flask import redirect, render_template, request, url_for
from application.topics.models import Topics
from application.topics.forms import TopicsForm
from application.categories.models import Categories

from flask_login import login_required, current_user


@app.route("/topics/new/<category_id>")
@login_required
def topics_form(category_id):
    return render_template(
        "topics/new.html", form=TopicsForm(), category_id=category_id)


@app.route("/topics/new/<category_id>/", methods=["POST"])
@login_required
def topics_create(category_id):
    k = Categories.query.get(category_id)
    form = TopicsForm(request.form)
    if not form.validate():
        return render_template("topics/new.html", form=form)
    t = Topics(form.name.data, form.desc.data)
    t.account_id = current_user.id
    k.aiheet.append(t)
    db.session().add(k)

    db.session().commit()

    return redirect(url_for("index"))

@app.route("/topics/<topic_id>")
@login_required
def topic_link(topic_id):
    return render_template(
        "topics/topic.html", topic_id=topic_id)