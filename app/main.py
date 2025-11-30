from fastapi import FastAPI
from app.core.database import engine, Base

# Criando a aplicação com o fastapi 
app = FastAPI(title="Diag Manager API", version="1.0.0")

# criando as tabelas do banco de dados ao iniciar a aplicação
Base.metadata.create_all(bind=engine)


# Rota raiz para verificar se a API está rodando corretamente
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Api esta rodando corretamente",
    }



