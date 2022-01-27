from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    userneme = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __init__(self, usserneme, password, name, email):
        self.usserneme = usserneme
        self.password = password
        self.name = name
        self.email = email

    def __repr(self):
        return "<User %r>" % self.usserneme

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    costent = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, content, user_id):
        self.costent = content
        self.user_id = user_id

    def __repr__(self):
        return "<post %r>" % self.id

class Follow(db.Model):
    __tablename__ = 'follow'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', foreign_Keys=user_id)
    follower = db.relationship('User', foreign_Keys=follower_id)
