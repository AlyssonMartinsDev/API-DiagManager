# imports necessarios para definir o modelo Client

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy.sql import func

class Clients(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80))
    phone_number = Column(String(20), nullable=False, unique=True)
    email = Column(String(150))
    cpf = Column(String(14))

    # city_id = Column(Integer, ForeignKey("city.id"))
    # company_id = Column(Integer, ForeignKey("company.id"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relacionamentos
    # city = relationship("City", back_populates="clients")
    # company = relationship("Company", back_populates="clients")



