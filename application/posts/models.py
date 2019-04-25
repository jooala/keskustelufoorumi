from application import db
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship, backref


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    message = db.Column(db.Text, nullable=False)
    account_id = db.Column(
        db.Integer, db.ForeignKey('account.id'), nullable=False)
    topics_id = db.Column(
        db.Integer, db.ForeignKey('topics.id'), nullable=False)    


    def __init__(self, message):
        self.message = message

    @staticmethod
    def find_posts(topic_id):
        stmt = text(
            "SELECT Posts.id, Posts.message, Account.username, Posts.date_created, Account.id FROM Posts "
            "LEFT JOIN Account ON Account.id = Posts.account_id "
            "LEFT JOIN Topics ON Topics.id = Posts.topics_id "
            "WHERE Topics.id = :topic").params(topic=topic_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({
                "id": row[0],
                "message": row[1],
                "username": row[2],
                "date": row[3],
                "userid": row[4],
            })
        return response

    @staticmethod
    def topics_info(topic_id):
        stmt = text(
            "SELECT Topics.id, Topics.name, Topics.desc FROM Topics "
            "WHERE Topics.id = :topic").params(topic=topic_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id": row[0], "name": row[1], "desc": row[2]})
        return response