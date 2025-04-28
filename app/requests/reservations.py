from fastapi import APIRouter, Depends, HTTPException, Body, Path
from sqlalchemy.orm import Session
from app.services.reservations_service import create_reservation, get_passanger_reservations, get_travel_reservations, get_reservation
from app.services.passangers_service import get_passenger_by_id
from app.services.travels_service import get_travel_by_code
from config.database import SessionLocal
from app.models.reservations import Reservation
import pdb

router = APIRouter()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close

@router.get("/", description="Get all reservations registers in database")
def get_all_reservations(db: Session = Depends(get_db)):
  return db.query(Reservation).all()

@router.get("/passenger/{id}", description="Get all reservations of a passenger seached by id")
def get_passenger_reservations_endpoint(db:Session = Depends(get_db), id: int = Path(..., examples={"default": {"summary": "Id example", "value": 1}})):
  passenger = get_passenger_by_id(db, id)
  if not passenger:
    raise HTTPException(status_code=404, detail="Passenger not found")
  return get_passanger_reservations(db, id)

@router.get("/travel/{code}", description="Get all reservations of a travel seached by code")
def get_travel_reservations_endpoint(db: Session = Depends(get_db), code: str = Path(..., examples={"default": {"summary": "Code example", "value": "Abc123"}})):
  travel = get_travel_by_code(db, code)
  if not travel:
    raise HTTPException(status_code=404, detail="Travel not found")
  return get_travel_reservations(db, code)

@router.post("/", description="Create a new reservation verifying if it doesn't exist by passenger id and travel code")
def create_reservation_endpoint(payload: dict = Body(
  ...,
  example={
    "passenger_id": 1,
    "travel_code": "Abc123"
  }), db: Session = Depends(get_db)):
  passenger_id = payload.get("passenger_id")
  travel_code = payload.get("travel_code")
  passenger = get_passenger_by_id(db, passenger_id)
  travel = get_travel_by_code(db, travel_code)
  if not passenger or not travel:
    raise HTTPException(status_code=400, detail="Passenger or travel not found")
  if get_reservation(db, passenger_id, travel.id):
    raise HTTPException(status_code=400, detail="Passenger already reserved this travel")
  new_reservation = create_reservation(db=db, passenger_id=passenger_id, travel_id=travel.id)
  return new_reservation
