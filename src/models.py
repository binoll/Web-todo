"""
Модуль, содержащий модели для задач (todos).
"""

from sqlalchemy import Column, Integer, Boolean, Text, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Todo(Base):
    """Модель задачи (Todo).

    Атрибуты:
        id (int): Уникальный идентификатор задачи (первичный ключ).
        title (str): Заголовок задачи.
        tag (str): Тег задачи. Может быть одним из: 'plans', 'study', 'personal'.
        description (str): Описание задачи.
        completed (bool): Статус выполнения задачи (по умолчанию False).

    Методы:
        __repr__: Возвращает строковое представление задачи.
    """
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    tag = Column(Enum('plans', 'study', 'personal'))
    description = Column(Text)
    completed = Column(Boolean, default=False)

    def __repr__(self):
        """Возвращает строковое представление задачи.

        Возвращает:
            str: Строка в формате 'Todo <id>'.
        """
        return f'Todo {self.id}'
