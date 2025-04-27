from sqlalchemy import Table, Column, Integer, String
from config.database import metadata

travels = Table(
    "travels",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("code", String(10)),
    Column("travel_from", String(100)),
    Column("travel_to", String(100)),
    Column("departure_date", String(100)),
)