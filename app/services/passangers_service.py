from sqlalchemy.orm import Session
from app.models.passengers import Passenger

def create_passenger(db: Session, name: str, last_name: str, birthdate: str):
  db_passenger = Passenger(name=name, last_name=last_name, birthdate=birthdate)
  db.add(db_passenger)
  db.commit()
  db.refresh(db_passenger)
  return db_passenger

def get_passenger_by_id(db: Session, id: int):
  return db.query(Passenger).filter(Passenger.id == id).first()

def update_passenger(db: Session, payload: dict, passenger: Passenger):
  allowed_fields = {"name", "last_name", "birthdate"}
  for key, value in payload.items():
    if key in allowed_fields:
      setattr(passenger, key, value)

  db.commit()
  db.refresh(passenger)
  return passenger