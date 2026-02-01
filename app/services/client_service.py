from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.client import Clients
from app.schemas.client_schema import ClientCreate


class ClientService:
    @staticmethod
    def create(db:Session, client_data: ClientCreate):
        
        
        # Primeira regra de negocio, o telefone deve ser unico
        existing_client = db.query(Clients).filter(Clients.phone_number == client_data.phone_number).first()

        if existing_client:
            raise HTTPException(status_code=400, detail="Numero de telefone ja cadastrado.")
        
            
        # Segunda regra de negocio, o email deve ser unico
        if client_data.email:
            existing_client = db.query(Clients).filter(Clients.email == client_data.email).first()
            if existing_client:
                raise HTTPException(status_code=400, detail="Email ja cadastrado.")
            
        # Terceira regra de negocio, se o cpf for fornecido, deve ser unico
        if client_data.cpf:
            existing_client = db.query(Clients).filter(Clients.cpf == client_data.cpf).first()
            if existing_client:
                raise HTTPException(status_code=400, detail="CPF ja cadastrado.")
        

        
              
        new_client = Clients(
            first_name=client_data.first_name,
            last_name=client_data.last_name,
            phone_number=client_data.phone_number,
            email=client_data.email,
            cpf=client_data.cpf

        )

        db.add(new_client)
        db.commit()
        db.refresh(new_client)

        
        return new_client

    @staticmethod
    def get_all(db: Session):
        return db.query(Clients).all()

















        
