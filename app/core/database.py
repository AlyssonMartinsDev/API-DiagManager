from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# definindo a url do sqlite e por padrao ele crial automaticamente o banco de dados na raiz do projeto

DATABASE_URL = "sqlite:///./diag_manager.db"


# ENGINE: a engine é a conexão principal com o banco de dados

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # necessário para sqlite
)


# SessionLocal: cria sessões de banco de dados individuais para cada solicitação
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base: classe base para os modelos ORM
Base = declarative_base()

# Função para obter uma sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

