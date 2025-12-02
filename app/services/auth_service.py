from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.security import verify_password
from app.utils.jwt_utils import create_access_token
from datetime import timedelta



class AuthService:

    # criando o metodo de autenticação do usuario
    @staticmethod
    def authenticate_user(db: Session, email: str, password: str):
        # Buscando no banco de dados um usuario pelo email
        user = db.query(User).filter(User.email == email).first()

        # Se não encontrar o usuario ou a senha estiver incorreta
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Email ou senha incorretos")
        
        return user
    
    # criando o metodo de login do usuario
    @staticmethod
    def login(db: Session, email:str, password: str):

        # Usando o proprio metodo de autenticação de usuario para validar o usuario
        user = AuthService.authenticate_user(db, email, password)

        # criando o token de acesso para o usuario autenticado
        token = create_access_token(
            data={"sub": str(user.id)},
            expires_delta=timedelta(hours=1)
        )

        # Retornando o token de acesso
        return {"access_token": token, "token_type": "bearer"}
    




