import os
from models.database import db_url
import create_database as db_creator



if __name__ == '__main__':
    db_is_created = os.path.exists(db_url)
    if not db_is_created:
        db_creator.create_db()