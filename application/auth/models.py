from application import db


class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    rank = db.Column(db.String(144), nullable=False)

    def __init__(self, name, username, password, rank):
        self.name = name
        self.username = username
        self.password = password
        self.rank = rank

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    def roles(self):
        return [self.rank]

    def has_rank(self):
        if self.rank == "ADMIN":
            return False

       
        