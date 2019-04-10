from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.posts.models import Posts
from application.posts.forms import PostsForm
from flask_login import current_user



@app.route("/topics/<topic_id>", methods=["POST"])
@login_required(role="ADMIN")
def message_create(topic_id):
    form = PostsForm(request.form)
    if not form.validate():
       return render_template(
        "topics/topic.html", topic_id=topic_id, form=form, find_posts=Posts.find_posts(topic_id), topics_info=Posts.topics_info(topic_id))
    t = Posts(form.message.data)
    t.account_id = current_user.id
    t.topics_id = topic_id
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("topic_link", topic_id=topic_id))

