from fastapi import APIRouter, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
from database.connection import SessionLocal
from database.schemas import Pet
from database import repository

router = APIRouter()


def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.get("/pets", response_model=List[Pet])
async def get_pets(db: Session = Depends(get_db)):
  pets = repository.get_pets(db)
  return JSONResponse(content=jsonable_encoder(pets),
                      status_code=status.HTTP_200_OK)
