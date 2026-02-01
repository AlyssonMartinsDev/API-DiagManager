from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional


# Classe base do client com configurações comuns
class ClientBase(BaseModel):
    first_name: str = Field(..., example="John")
    last_name : Optional[str] = Field(None, example="Doe")
    phone_number: str = Field(..., example="+1234567890")
    email: Optional[EmailStr] = Field(None, example="")
    cpf: Optional[str] = Field(None, example="123.456.789-00")



class ClientCreate(ClientBase):
    model_config = ConfigDict(from_attributes=True)


    

