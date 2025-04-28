from fastapi import FastAPI
from app.requests import travels, passengers, reservations
app = FastAPI(title="API for reservations", version="1.0.0")

app.include_router(travels.router, prefix="/travels", tags=["Travels"])
app.include_router(passengers.router, prefix="/passengers", tags=["Passengers"])
app.include_router(reservations.router, prefix="/reservations", tags=["Reservations"])
