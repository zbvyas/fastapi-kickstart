from fastapi import APIRouter, status, Depends, Path
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
from database.connection import SessionLocal
from database.schemas import Pet, PetBase
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


@router.get("/pets/{pet_id}", response_model=Pet)
async def get_pet(
    pet_id: int = Path(..., title="The ID of the pet to get"),
    db: Session = Depends(get_db)
  ):
  pet = repository.get_pet(pet_id, db)
  return JSONResponse(content=jsonable_encoder(pet),
                      status_code=status.HTTP_200_OK)


@router.post("/pets", response_model=Pet)
async def create_pet(pet: PetBase, db: Session = Depends(get_db)):
  result = repository.create_pet(pet, db)
  return JSONResponse(content=jsonable_encoder(result),
                      status_code=status.HTTP_201_CREATED)

# TODO
@router.put("/pets/{pet_id}", response_model=Pet)
async def update_pet(
    pet: PetBase,
    pet_id: int = Path(..., title="The ID of the pet to update"),
    db: Session = Depends(get_db)
  ):
  result = repository.update_pet(pet_id, pet, db)
  return JSONResponse(content=jsonable_encoder(result),
                      status_code=status.HTTP_200_OK)


@router.delete("/pets/{pet_id}")
async def delete_pet(
    pet_id: int = Path(..., title="The ID of the pet to delete"),
    db: Session = Depends(get_db)
  ):
  result = repository.delete_pet(pet_id, db)
  return JSONResponse(content={'message': f'Successfully deleted pet ID {result}'},
                      status_code=status.HTTP_200_OK)
