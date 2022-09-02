from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.student import Student

from models.database import Base

class Group(Base):
    __tablename__ = 'groups'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    group_name = Column(String)
    student = relationship(Student)

    def __repr__(self):
        return f'Группа [ID: {self.id}, Название: {self.group_name}]'

