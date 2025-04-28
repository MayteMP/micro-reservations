from sqlalchemy.orm import Session
from app.models.reservations import Reservation


def create_reservation(db: Session, passenger_id: str, travel_id: str):
  db_reservation = Reservation(passenger_id=passenger_id, travel_id=travel_id)
  db.add(db_reservation)
  db.commit()
  db.refresh(db_reservation)
  return db_reservation

def get_passanger_reservations(db: Session, passenger_id: str):
  return db.query(Reservation).filter(Reservation.passenger_id == passenger_id).all()

def get_travel_reservations(db: Session, travel_id: str):
  return db.query(Reservation).filter(Reservation.travel_id == travel_id).all()

def get_reservation(db: Session, passenger_id: str, travel_id: str):
  return db.query(Reservation).filter(Reservation.passenger_id == passenger_id, Reservation.travel_id == travel_id).first()
