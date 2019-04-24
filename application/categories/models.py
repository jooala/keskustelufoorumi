from application import db
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship, backref


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    desc = db.Column(db.String(144), nullable=True)

    aiheet = relationship("Topics", secondary="topics_categories")

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    @staticmethod
    def find_categories():
        stmt = text(
            "SELECT Categories.id, Categories.name, Categories.desc, COUNT(Topics.id), COUNT(Posts.id) FROM Categories "
            "LEFT JOIN topics_categories ON topics_categories.categories_id = Categories.id "
            "LEFT JOIN Topics ON Topics.id = topics_categories.topics_id "
            "LEFT JOIN Posts ON Posts.topics_id = Topics.id "
            "GROUP BY Categories.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({
                "id": row[0],
                "name": row[1],
                "desc": row[2],
                "count": row[3],
                "message_count": row[4],
            })
        return response

