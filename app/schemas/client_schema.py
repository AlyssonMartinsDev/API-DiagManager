from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from pydantic import field_validator


# Classe base do client com configurações comuns
class ClientBase(BaseModel):
    first_name: str = Field(..., example="John")
    last_name : Optional[str] = Field(None, example="Doe")
    phone_number: str = Field(..., example="+1234567890")
    email: Optional[EmailStr] = Field(None, example="")
    cpf: Optional[str] = Field(None, example="123.456.789-00")

    @field_validator("first_name", "phone_number")
    @classmethod
    def not_blank(cls, v:str):
        v = v.strip()

        if not v:
            raise ValueError("Os campos nome e telefone são obrigatorios.")
        return v 

    @field_validator("last_name", "email", "cpf", mode="before")
    @classmethod
    def empty_to_none(cls, v):
        if v is None:
            return None
        if isinstance(v, str) and not v.strip():
            return None
        return v

class ClientCreate(ClientBase):
    model_config = ConfigDict(from_attributes=True)


class ClientResponse(ClientBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

    

