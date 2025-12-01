from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Gera a has da senha
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Verifica se a senha corresponde ao hash
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)