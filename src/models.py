"""
Tasks models
"""
from sqlalchemy import Column, Integer, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Todo(Base):
	"""
    Todo model
    """
	__tablename__ = 'todos'
	id = Column(Integer, primary_key=True)
	task = Column(Text)
	completed = Column(Boolean, default=False)

	def __repr__(self):
		return f'<Todo {self.id}>'
