from sqlalchemy import Table, Column, Integer, String
from config.database import Base
from datetime import datetime

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    passenger_id = Column(String(10))
    travel_id = Column(String(10))
    register_time = Column(String(100))
