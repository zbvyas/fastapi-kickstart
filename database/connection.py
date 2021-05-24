from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from os import environ

vars = load_dotenv()
user = environ.get('PETS_DATABASE_USER')
password = environ.get('PETS_DATABASE_PASSWORD')
url = environ.get('PETS_DATABASE_URL')

SQLALCHEMY_DATABASE_URL = "mysql://{}:{}@{}/pets_development".format(user, password, url)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()