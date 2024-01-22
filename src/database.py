"""
Database for storing todos
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base

DB_PATH = 'database'
DB_URL = os.path.join('sqlite:///', DB_PATH, 'db.sqlite')
ENGINE = create_engine(DB_URL, connect_args={'check_same_thread': False})
SESSION = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)


def init_db():
    """
    Init database, create all models as tables
    """
    if not os.path.exists(DB_PATH) or not os.path.isdir(DB_PATH):
        os.mkdir(DB_PATH)

    Base.metadata.create_all(bind=ENGINE)


def get_db():
    """
    Create session/connection for each request
    """
    database = SESSION()

    try:
        yield database
    finally:
        database.close()
