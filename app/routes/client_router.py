from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.client_schema import ClientCreate
from app.services.client_service import ClientService

router = APIRouter(
    prefix="/clients",
    tags=["Clients"]
)

@router.get("/")
def get_all_clients(depends_db: Session = Depends(get_db)):
    return ClientService.get_all(db=depends_db)

@router.post("/", status_code=201)
def create_client(client_data: ClientCreate, depends_db: Session = Depends(get_db)):

    return ClientService.create(db=depends_db, client_data=client_data)
    

    
