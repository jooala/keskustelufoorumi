from application import db

<<<<<<< HEAD

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
=======
class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
>>>>>>> 737aaca... muutoksia kirjautumiseen sekä layouttiin

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
<<<<<<< HEAD

=======
  
>>>>>>> 737aaca... muutoksia kirjautumiseen sekä layouttiin
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True