from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

database_protocol = 'sqlite:///store/database.db'
engine = create_engine(database_protocol)
session = sessionmaker(bind=engine)


def generate_session():
    sess: Session = session()
    try:
        yield sess
    finally:
        sess.close()
