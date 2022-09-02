from sqlalchemy import Column, Integer, String, ForeignKey

from models.database import Base

class Student(Base):
    __tablename__ = 'student'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    age = Column(Integer)
    address = Column(String)
    group = Column(Integer, ForeignKey('group_id'))

    def __int__(self, full_name: str, age: int, address: str, group_id: int):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.age = age
        self.address = address
        self.group = group_id

    def __repr__(self):
        info: str = f'Студент [ФИО: {self.surname} {self.name} {self.patronymic},' \
                    f'Возраст: {self.age}, Адрес: {self.address}, ID группы: {self.group}]'
        return info

