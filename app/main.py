from fastapi import FastAPI

# Criando a aplicação com o fastapi 
app = FastAPI(title="Diag Manager API", version="1.0.0")


# Rota raiz para verificar se a API está rodando corretamente
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Api esta rodando corretamente",
    }