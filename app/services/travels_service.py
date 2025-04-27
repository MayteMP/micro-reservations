from sqlalchemy.orm import Session
from app.models.travels import Travel

def create_travel(db: Session, code: str, travel_from: str, travel_to: str, departure_date: str):
  db_travel = Travel(code=code, travel_from=travel_from, travel_to=travel_to, departure_date=departure_date)
  db.add(db_travel)
  db.commit()
  db.refresh(db_travel)
  return db_travel

def get_travel_by_code(db: Session, code: str):
  return db.query(Travel).filter(Travel.code == code).first()

def update_travel(db:Session, payload: dict, travel: Travel):
  allowed_fields = {"code", "travel_from", "travel_to", "departure_date"}
  for key, value in payload.items():
    if key in allowed_fields:
      setattr(travel, key, value)

  db.commit()
  db.refresh(travel)
  return travel