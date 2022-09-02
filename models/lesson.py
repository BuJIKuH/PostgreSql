from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base
from models.group import Group

association_table = Table('association', Base.metadata,
                          Column('lesson_id', Integer, ForeignKey('lessons.id'), primary_key=True),
                          Column('group_id', Integer, ForeignKey('groups.id'), primary_key=True)
                          )

class Lesson(Base):
    __tablename__ = 'lessons'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    lesson_title = Column(String)
    groups = relationship(Group, secondary=association_table, backref='group_lesson')

    def __repr__(self):
        return f'Группа [ID: {self.id}, Название: {self.lesson_title}]'