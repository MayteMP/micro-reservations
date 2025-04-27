from sqlalchemy import Table, Column, Integer, String
from config.database import metadata
from datetime import datetime

reservations = Table(
    "reservations",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("passanger_id", String(10), foreignKey="passengers.id"),
    Column("travel_id", String(10), foreignKey="travels.id"),
    Column("register_time", datetime.utcnow)
)