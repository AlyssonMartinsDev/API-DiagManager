from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.user import User
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdate

from app.utils.security import hash_password

# criando a classe de serviço para o usuário
class UserService:


    # método para criar um novo usuário
    @staticmethod
    def create_user(db: Session, user_create: UserCreate):

        # Regra de negocio 1: Email deve ser único
        existing_user = db.query(User).filter(User.email == user_create.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email já cadastrado.")
        

        password_hashed = hash_password(user_create.password)
        
        # Cria um novo usuario ( convertendo o schema para o modelo)
        new_user = User(
            username = user_create.username,
            email = user_create.email,
            full_name = user_create.full_name,
            hashed_password = password_hashed
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    
    # método para obter todos os usuarios
    @staticmethod
    def get_all_users(db: Session):
        return db.query(User).all()
    
    # metodo para obter um usuário por ID
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> UserResponse:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")
        return user
    
    # metodo para atualizar um usuário (exemplo adicional)
    @staticmethod
    def update_user(db: Session, user_id: int, user_data: UserUpdate) -> UserResponse:

        # Primeira regra de negócio: Verificar se o usuário existe se não existir, lançar um erro 404
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")
        
        # atualizando o username caso ele seja enviado

        if user_data.username is not None:
            user.username = user_data.username

        # atualizadno o email caso ele seja enviado
        if user_data.email is not None:
            
            # Regra de negocio 2: Email deve ser único
            exists = db.query(User).filter(
                User.email == user_data.email,
                User.id != user_id
            ).first()

           

            if exists:
                raise HTTPException(status_code=400, detail="Email já cadastrado.")
            
            user.email = user_data.email
        
        # atualizando o full_name caso ele seja enviado
        if user_data.full_name is not None:
            user.full_name = user_data.full_name

        # salvando as alterações no banco de dados
        db.commit()
        db.refresh(user)

        return user
        