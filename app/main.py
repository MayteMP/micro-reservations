from fastapi import FastAPI, Request, HTTPException
from config.database import database, engine, metadata
from app.models.passengers import passengers
from datetime import datetime
from contextlib import asynccontextmanager

metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
  await database.connect()
  yield
  await database.disconnect()

app = FastAPI(lifespan=lifespan)