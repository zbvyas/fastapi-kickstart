from database.models import Pet
from sqlalchemy.orm import Session


def get_pets(db: Session):
    return db.query(Pet).all()


def get_pet(pet_id: int, db: Session):
    return db.query(Pet).filter(Pet.id == pet_id).first()


def create_pet(pet: Pet, db: Session):
    new_pet = Pet(**pet.dict())
    db.add(new_pet)
    db.commit()
    db.refresh(new_pet)
    return new_pet


def update_pet(pet_id: int, pet: Pet, db: Session):
    updated_pet = Pet(**pet.dict())
    db.query(Pet).filter(Pet.id == pet_id).update(updated_pet)
    db.commit()
    db.refresh(updated_pet)
    return updated_pet


def delete_pet(pet_id: int, db: Session):
    db.query(Pet).filter(Pet.id == pet_id).delete()
    db.commit()
    return pet_id
