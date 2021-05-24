# Pydantic Models - defines the "schema" (data validation)

from pydantic import BaseModel

class Pet(BaseModel):
  id: int
  name: str
  color: str
  breed: str

  class Config:
    orm_mode = True
