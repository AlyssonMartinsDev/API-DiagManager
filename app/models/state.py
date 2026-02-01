from sqlalchemy import Column, Integer, String
from app.core.database import Base



class State(Base):
    __tablename__ = "state"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    uf = Column(String(2), nullable=False, unique=True)

