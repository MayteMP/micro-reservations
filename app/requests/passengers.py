from fastapi import APIRouter, Depends, HTTPException, Body, Path
from sqlalchemy.orm import Session
from app.services.passangers_service import create_passenger, get_passenger_by_id, update_passenger
from config.database import SessionLocal
from app.models.passengers import Passenger
from dotenv import load_dotenv
import os
import httpx

load_dotenv('.env')
external_url = os.getenv("EXTERNAL_URL")

router = APIRouter()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.get("/", description="Get all passengers registers in database")
def get_all_passengers(db: Session = Depends(get_db)):
  return db.query(Passenger).all()

@router.get("/{id}", description="Get all information of passenger seached by id")
def get_passenger_endpoint(id: int = Path(..., examples={"default": {"summary": "Id example", "value": 1}}), 
                        db: Session = Depends(get_db)):
  find_passenger = get_passenger_by_id(db, id)
  if find_passenger is None:
    raise HTTPException(status_code=404, detail="Passenger not found")
  return find_passenger

@router.post("/", description="Create a new passenger verifying if it doesn't exist by id")
def create_passenger_endpoint(payload: dict = Body(
  ...,
  example={
    "name": "John",
    "last_name": "Doe",
    "birthdate": "1990-01-01"
  }), db: Session = Depends(get_db)):
  name = payload.get("name")
  last_name = payload.get("last_name")
  birthdate = payload.get("birthdate")
  if not name or not last_name or not birthdate:
    raise HTTPException(status_code=400, detail="Missing required fields")
  new_passenger = create_passenger(db=db, name=name, last_name=last_name, birthdate=birthdate)
  return new_passenger

@router.put(
    "/{id}",
    description="Update passenger information by id."
)
def update_passenger_endpoint(
  id: int = Path(..., description="Id of the passenger to be updated"),
  payload: dict = Body(
    ...,
    example={
        "name": "John",
        "last_name": "Doe",
        "birthdate": "1990-01-01"
    }),
  db: Session = Depends(get_db)):
  passenger = get_passenger_by_id(db, id)
  if not passenger:
      raise HTTPException(status_code=404, detail="Passenger not found")

  updated_passenger = update_passenger(db=db, payload=payload, passenger=passenger)
  return update_external(payload, updated_passenger)


def update_external(payload, passenger):
  data = {
    "name": payload.get("name"),
    "last_name": payload.get("last_name"),
    "birthdate": payload.get("birthdate")
  }

  with httpx.Client() as client:
    client.put(external_url + 'passengers/'+ str(passenger.id), json=data)
  return passenger
