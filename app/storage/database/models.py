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


class Worker(db.Model):
    __tablename__ = 'workers'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    role = db.Column(db.String(16))
    user = db.relationship("User", backref=db.backref("users", uselist=False))


class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    description = db.Column(db.String(1024))
    positions = db.relationship('Position', lazy='select', backref=db.backref('restaurant', lazy='joined'))

    def __str__(self):
        return 'Restaurant <{0}>'.format(self.id)


class Menu(db.Model):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    description = db.Column(db.String(1024))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    restaurant = db.relationship("Restaurant", backref=db.backref("menus", uselist=False))
    positions = db.relationship('MenuPosition', lazy='select', backref=db.backref('menu', lazy='joined'))

    def __str__(self):
        return 'Menu <{0}>'.format(self.id)


class Position(db.Model):
    __tablename__ = 'positions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    description = db.Column(db.String(1024))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    menus = db.relationship('MenuPosition', lazy='select', backref=db.backref('position', lazy='joined'))

    def __str__(self):
        return 'Position <{0}>'.format(self.id)


class MenuPosition(db.Model):
    __tablename__ = 'menu_positions'

    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'), primary_key=True)
    position_id = db.Column(db.Integer, db.ForeignKey('positions.id'), primary_key=True)
    cost = db.Column(db.NUMERIC, default=0)

    def __str__(self):
        return 'MenuPosition <{0}, {1}>'.format(self.menu_id, self.position_id)


class Invitation(db.Model):
    __tablename__ = 'invitations'

    id = db.Column(db.Integer, primary_key=True)
