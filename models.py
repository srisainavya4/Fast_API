from sqlalchemy import String, Integer, Column, Float, DateTime
from database import Base, engine

def create_tables():
    Base.metadata.create_all(engine)

class Invoice (Base):
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key=True)
    number = Column(String(40), nullable=False)
    amount = Column(Float, nullable=False)
    instatus = Column(String(20), nullable=False)
    date = Column(DateTime, nullable=False)