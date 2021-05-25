# Pydantic Models - defines the "schema" (data validation)
from pydantic import BaseModel


class PetBase(BaseModel):
  name: str
  color: str
  breed: str


class Pet(PetBase):
  id: int
  name: str
  color: str
  breed: str

  class Config:
    orm_mode = True
