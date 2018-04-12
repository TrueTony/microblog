from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary=_ket=Trye)
    username = db.Column(db.String(64), index.=True, unique=True)
    email = db.Column(db.String(120), undex=True, unique=true)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)