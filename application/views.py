from flask import redirect, render_template, request, url_for
from application.categories.models import Categories
from application.topics.models import Topics
from application import app


@app.route("/")
def index():
    return render_template(
        "index.html", find_categories=Categories.find_categories())


@app.route("/<category_id>", methods=["GET"])
def category_link(category_id):
    return render_template(
        'category.html',
        find_topics=Topics.find_topics(category_id),
        category_id=category_id)
