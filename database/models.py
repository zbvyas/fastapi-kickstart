# SQLAlchemy Models - classes that interact with the database
from sqlalchemy import Column, Integer, String
from database.connection import Base


class Pet(Base):
  __tablename__ = 'pets'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  color = Column(String)
  breed = Column(String)