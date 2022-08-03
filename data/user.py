import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


# объекты класса пользователь
class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'user'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    tg_id = sqlalchemy.Column(sqlalchemy.Integer)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    balance = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    slovo = sqlalchemy.Column(sqlalchemy.String, default="")
    good = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    bad = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    error = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    msg = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    bad_slova = sqlalchemy.Column(sqlalchemy.String, default="0 " * 600)
    id_slova = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    tren = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    nedel = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    buy = sqlalchemy.Column(sqlalchemy.Integer, default=0)

    def __repr__(self):
        return f'<User> {self.id} {self.name}'
