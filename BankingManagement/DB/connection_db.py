import os
import dotenv

from sqlalchemy import create_engine
from urllib.parse import quote_plus

dotenv.load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
# encoding to URL-encoded characters
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
DB_NAME = os.getenv("DB_NAME")


def get_connection():
    my_url = "mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

    return create_engine(url=my_url)
