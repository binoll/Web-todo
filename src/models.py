"""
Tasks models
"""
from sqlalchemy import Column, Integer, Boolean, Text, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Todo(Base):
	"""
    Task model
    """
	__tablename__ = 'todos'
	id = Column(Integer, primary_key=True)
	title = Column(Text)
	tag = Column(Enum('plans', 'study', 'personal'))
	description = Column(Text)
	completed = Column(Boolean, default=False)
	
	def __repr__(self):
		return f'Todo {self.id}'
