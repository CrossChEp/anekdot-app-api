from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

base = declarative_base()


class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    liked = relationship('Liked', backref='user')


class Liked(base):
    __tablename__ = 'liked'
    id = Column(Integer, primary_key=True)
    users_liked = Column(Integer, ForeignKey('users.id'))
