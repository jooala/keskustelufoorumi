from application import db
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship


class Topics(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    desc = db.Column(db.String(144), nullable=True)

    account_id = db.Column(
        db.Integer, db.ForeignKey('account.id'), nullable=False)

    kategoriat = relationship("Categories", secondary="topics_categories")

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    @staticmethod
    def find_topics(category_id):
        stmt = text(
            "SELECT Topics.id, Topics.name, Topics.desc FROM Topics "
            "LEFT JOIN topics_categories ON topics_categories.topics_id = Topics.id "
            "LEFT JOIN Categories ON Categories.id = topics_categories.categories_id "
            "WHERE Categories.id = :category").params(category=category_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id": row[0], "name": row[1], "desc": row[2]})
        return response

    @staticmethod
    def topic_amount(category_id):
        stmt = text(
            "SELECT COUNT(*) FROM Topics "
            "LEFT JOIN topics_categories ON topics_categories.topics_id = Topics.id "
            "LEFT JOIN Categories ON Categories.id = topics_categories.categories_id "
            "WHERE Categories.id = :category").params(category=category_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"count": row[0]})
        return response