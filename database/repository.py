from database.models import Pet
from sqlalchemy.orm import Session

def get_pets(db: Session):
    return db.query(Pet).all()