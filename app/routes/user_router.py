from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from app.services.user_service import UserService

from app.utils.jwt_utils import get_current_user

# definindo o roteador para as rotas de usuário
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# rota de criar usuário
@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(db, user_create)


# rota para obter todos os usuários
@router.get("/", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return UserService.get_all_users(db)

# rota para obter um usuário por ID (exemplo adicional)
@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(
    user_id: int, 
    db: Session = Depends(get_db), 
    current_user=Depends(get_current_user)
):
    return UserService.get_user_by_id(db, user_id)

# rota para atualizar um usuário por ID (exemplo adicional)
@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    return UserService.update_user(db, user_id, user_update)

    