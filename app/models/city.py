from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy.sql import func

class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)

    # Relacionamentos
    state = relationship("State", back_populates="city")