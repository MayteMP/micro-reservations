from sqlalchemy import Table, Column, Integer, String
from config.database import Base

class Passenger(Base):
    __tablename__ = "passengers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    last_name = Column(String(100))
    birthdate = Column(String(100))
