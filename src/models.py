"""
Tasks models
"""
from sqlalchemy import Column, Integer, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Task(Base):
	"""
    Task model
    """
	__tablename__ = 'tasks'
	id = Column(Integer, primary_key=True)
	text = Column(Text)
	completed = Column(Boolean, default=False)

	def __repr__(self):
		return f'<Task {self.id}>'
