from fastapi import FastAPI
from app.core.database import engine, Base
from app.routes.user_router import router as user_router
from app.routes.auth_router import router as auth_router


# importando os modelos para garantir que as tabelas sejam criadas
from app.models import user

# Criando a aplicação com o fastapi 
app = FastAPI(title="Diag Manager API", version="1.0.0")

# criando as tabelas do banco de dados ao iniciar a aplicação
Base.metadata.create_all(bind=engine)

# incluindo as rotas na aplicação
app.include_router(auth_router)
app.include_router(user_router)


# Rota raiz para verificar se a API está rodando corretamente
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Api esta rodando corretamente",
    }



