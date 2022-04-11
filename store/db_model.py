from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

base = declarative_base()


class AnekdotAndUserRelation(base):
    __tablename__ = 'anekdot_and_user_relation'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    anekdot_id = Column(Integer, ForeignKey('anekdots.id'))


class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    anekdots = relationship('Anekdot', backref='user')
    liked = relationship('AnekdotAndUserRelation', backref='user')


class Anekdot(base):
    __tablename__ = 'anekdots'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    author = Column(Integer, ForeignKey('users.id'))
    liked_users = relationship('AnekdotAndUserRelation', backref='anekdot')
