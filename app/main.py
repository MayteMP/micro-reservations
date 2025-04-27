from fastapi import FastAPI
from app.requests import travels

app = FastAPI(title="API for reservations", version="1.0.0")

app.include_router(travels.router, prefix="/travels", tags=["Travels"])
