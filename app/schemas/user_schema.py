from pydantic import BaseModel, EmailStr, Field, model_validator as validator
from typing import Optional



# criando a classe base do usuário
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, title="Nome de usuário", examples={"exemplo": "johndoe"})
    email: EmailStr = Field(..., title="Endereço de e-mail", examples={"exemplo": "johndoe@gmail.com" })
    full_name: Optional[str] = Field(None, max_length=100, title="Nome completo", examples={"exemplo": "John Doe"})
    

# criando a classe para criação de usuário
class UserCreate(UserBase):
    password: str = Field(..., min_length=6, max_length=72,title="Senha do usuário", examples={"exemplo": "strongpassword123"})
    confirm_password: str = Field(..., min_length=6, title="Confirmação da senha", examples={"exemplo": "strongpassword123"})

    # validadno se as senhas coincidem
    @validator(mode="after")
    def passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("As senhas não coincidem.")
        return self
        

# criando a classe para resposta de usuário
class UserResponse(UserBase):
    id: int = Field(..., title="ID do usuário", examples={"exemplo": 1})
    hashed_password: str = Field(..., title="Senha criptografada do usuário")

    class Config:
        orm_mode = True

# criando a classe para atualização de usuário
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
