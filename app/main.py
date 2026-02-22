from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base
from app.routes.user_router import router as user_router
from app.routes.auth_router import router as auth_router
from app.routes.client_router import router as client_router

from fastapi.exceptions import RequestValidationError
from app.core.exception_handlers import (
    validation_exception_handler,
    http_exception_handler,
)


# importando os modelos para garantir que as tabelas sejam criadas
from app.models import user


# Criando a aplicação com o fastapi 
app = FastAPI(title="Diag Manager API", version="1.0.0")

# adicionando o interceptador de erros para os erros do pydantic e padronizar a resposta
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException,http_exception_handler)

# Criando o cors
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)

# criando as tabelas do banco de dados ao iniciar a aplicação
Base.metadata.create_all(bind=engine)

# incluindo as rotas na aplicação
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(client_router)


# Rota raiz para verificar se a API está rodando corretamente
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Api esta rodando corretamente",
    }



