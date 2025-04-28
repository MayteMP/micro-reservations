from sqlalchemy import Table, Column, Integer, String
from config.database import Base

class Travel(Base):
    __tablename__ = "travels"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10))
    travel_from = Column(String(100))
    travel_to = Column(String(100))
    departure_date = Column(String(100))
