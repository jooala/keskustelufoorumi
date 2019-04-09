from application import db
from sqlalchemy.orm import relationship, backref
from application.topics.models import Topics
from application.categories.models import Categories


class TopicsCategories(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    topics_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    categories_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    topic = relationship(
        Topics,
        backref=backref("topics_categories", cascade="all, delete-orphan"))
    category = relationship(
        Categories,
        backref=backref("topics_categories", cascade="all, delete-orphan"))
