from datetime import datetime, timedelta
from jose import jwt, JWTError

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User

SECRET_KEY = "DiagExpertsSecretKey"
ALGORITHM = "HS256"
ACSESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Função para obter o usuario atual a partir do token de acesso
def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
    payload = verify_access_token(token)

    # Se o token for inválido, lança uma exceção
    if payload is None:
        raise HTTPException(status_code=401, detail="Token de acesso inválido")
    
    # Pegando o ID do usuario do payload do token
    user_id: str = payload.get("sub")

    # Buscando o usuario no banco de dados pelo ID
    user = db.query(User).filter(User.id == int(user_id)).first()

    # Se o usuario não for encontrado, lança uma exceção
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user



# Função para um token de acesso com tempo de expiração
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACSESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) 

# Função para verificar e decodificar o token de acesso
def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
    