from faker import Faker

from models.database import create_db, Session
from models.lesson import Lesson
from models.student import Student
from models.group import Group



def create_database(load_fake_data: bool = True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())

def _load_fake_data(session: Session):
    pass