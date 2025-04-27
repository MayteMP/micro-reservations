from fastapi import APIRouter, Depends, HTTPException, Body, Path
from sqlalchemy.orm import Session
from app.services.travels_service import create_travel, get_travel_by_code, update_travel
from config.database import SessionLocal
from app.models.travels import Travel

router = APIRouter()

# Función para obtener la sesión de base de datos
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@router.get("/", description="Get all travels registers in database")
def get_all_travels(db: Session = Depends(get_db)):
  return db.query(Travel).order_by(Travel.id).all()

@router.get("/{code}", description="Get all information of travel seached by code")
def get_travel_endpoint(code: str = Path(..., examples={"default": {"summary": "Code example", "value": "Abc123"}}), 
                        db: Session = Depends(get_db)):
  find_travel = get_travel_by_code(db, code)
  if find_travel is None:
    raise HTTPException(status_code=404, detail="Travel not found")
  return find_travel
  
@router.post("/", description="Create a new travel verifying if it doesn't exist by id")
def create_travel_endpoint(payload: dict = Body(
  ...,
  example={
    "code": "Abc123",
    "travel_from": "Oaxaca",
    "travel_to": "Puebla",            
    "departure_date": "2023-01-01 10:00",
  }), db: Session = Depends(get_db)):
  code = payload.get("code")
  travel_from = payload.get("travel_from")
  travel_to = payload.get("travel_to")
  departure_date = payload.get("departure_date")
  if not code or not travel_from or not travel_to or not departure_date:
    raise HTTPException(status_code=400, detail="Missing required fields")
  find_travel = get_travel_by_code(db, code)
  if find_travel:
     raise HTTPException(status_code=400, detail="Travel already registered")
  new_travel = create_travel(db=db, code=code, travel_from=travel_from, travel_to=travel_to, departure_date=departure_date)
  return new_travel

@router.put(
    "/{code}",
    description="Update travel information by code."
)
def update_travel_endpoint(
  code: str = Path(..., description="Code of the travel to be updated"),
  payload: dict = Body(
    ...,
    example={
        "code": "Abc123",
        "travel_from": "Puebla",
        "travel_to": "San Luis Potosí",
        "departure_date": "2023-05-10 15:30"
    }),
  db: Session = Depends(get_db)):
  travel = get_travel_by_code(db, code)
  if not travel:
      raise HTTPException(status_code=404, detail="Travel not found")

  updated_travel = update_travel(db=db, payload=payload, travel=travel)
  return updated_travel