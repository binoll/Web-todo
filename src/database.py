"""
Модуль для работы с базой данных, предназначенной для хранения задач (todos).
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
    """Инициализирует базу данных и создает все таблицы на основе моделей.

    Если директория для базы данных не существует, она будет создана.
    """
    if not os.path.exists(DB_PATH) or not os.path.isdir(DB_PATH):
        os.mkdir(DB_PATH)

    Base.metadata.create_all(bind=ENGINE)


def get_db():
    """Создает сессию подключения к базе данных для каждого запроса.

    Используется как генератор, чтобы автоматически закрывать сессию после завершения работы.

    Yields:
        Session: Сессия подключения к базе данных.

    Пример использования:
        db = next(get_db())
    """
    database = SESSION()

    try:
        yield database
    finally:
        database.close()
