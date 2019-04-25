from flask_login import current_user
from application import app, db, login_required
from flask import redirect, render_template, request, url_for, flash
from application.auth.models import User
from application.profile.forms import ProfilesForm


@app.route("/user/<user_id>")
def user_link(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    return render_template(
        "users/profile.html", user=user, user_id=user_id, user_info=User.user_info(user_id))

@app.route("/user/edit/<user_id>")
def user_editlink(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    return render_template(
        "users/profileedit.html", user=user, user_info=User.user_info(user_id))


@app.route("/user/edit/<user_id>", methods=["POST"])
@login_required(role="ANY")
def profile_edit_name(user_id):
    form = ProfilesForm(request.form)
    
    if not form.validate():
        return render_template("users/profile.html", user_id=user_id)
    t = User.query.get(user_id)
    if t.id != current_user.id:
        flash('Et voi muuttaa toisen käyttäjän tietoja!')
        return redirect(url_for('user_link', user_id=user_id))
    else:
        t.name = request.form.get("name")
        db.session().commit()
        return redirect(url_for('user_link', user_id=user_id))