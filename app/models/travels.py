from sqlalchemy import Table, Column, Integer, String, MetaData
from config.database import Base
metadata = MetaData()

class Travel(Base):
    __tablename__ = "travels"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10))
    travel_from = Column(String(100))
    travel_to = Column(String(100))
    departure_date = Column(String(100))

# travels_table = Table(
#     "travels",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("code", String(10)),
#     Column("travel_from", String(100)),
#     Column("travel_to", String(100)),
#     Column("departure_date", String(100)),
# )
