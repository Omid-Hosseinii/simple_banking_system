from DB.connection_db import get_connection
from sqlalchemy.orm import sessionmaker



def get_session():
    engine = get_connection()
    session = sessionmaker(bind=engine)

    return session()
