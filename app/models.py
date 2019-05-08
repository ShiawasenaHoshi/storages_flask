import tarantool
from clickhouse_sqlalchemy import types, engines
from sqlalchemy import Column
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from config import Config


class User(db.Model):
    __bind_key__ = 'pgsql'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Rate(db.Model):
    __bind_key__ = 'clickhouse'
    day = Column(types.Date, primary_key=True)
    value = Column(types.Int32)

    __table_args__ = (
        engines.Memory(),
    )


class Place:
    conn = tarantool.connect(Config.TARANTOOL_HOST, Config.TARANTOOL_PORT)
    space_name = "place"

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Place):
            return self.code == other.code and self.name == other.name
        return False

    def save(self):
        if not self.code or not self.name:
            raise ValueError('empty code or name')
        else:
            Place.conn.insert(Place.space_name, (self.code, self.name))

    @staticmethod
    def search(code):
        result = Place.conn.select(Place.space_name, code)
        if result.rowcount > 0:
            return Place(result[0][0], result[0][1])
        else:
            return None

    @staticmethod
    def delete(place):
        Place.conn.delete(Place.space_name, place.code)
