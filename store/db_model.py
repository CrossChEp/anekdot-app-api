from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

base = declarative_base()


AnekdotAndUserRelation = Table(
    'anekdot_and_user_relation',
    base.metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('anekdot_id', Integer, ForeignKey('anekdots.id'))
)


class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    anekdots = relationship('Anekdot', backref='user')
    liked = relationship('Anekdot', secondary=AnekdotAndUserRelation, backref='user_liked')


class Anekdot(base):
    __tablename__ = 'anekdots'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    author = Column(Integer, ForeignKey('users.id'))
    liked_users = relationship('User', secondary=AnekdotAndUserRelation, backref='anekdot')
