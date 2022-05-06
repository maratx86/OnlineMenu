import datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app.storage import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(124), unique=True)
    firstname = db.Column(db.String(124), index=True)
    lastname = db.Column(db.String(124), index=True)
    username = db.Column(db.String(124), index=True, unique=True)
    password = db.Column(db.String(124), index=True)
    reg_date = db.Column(db.DATETIME, default=datetime.datetime.utcnow)

    @property
    def fullname(self):
        if self.lastname:
            return "{} {}".format(self.lastname, self.firstname)
        return self.firstname

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def change_password(self, password):
        self.password = generate_password_hash(password)
        db.session.commit()

    def __str__(self):
        return 'User <{0}>'.format(self.email)
