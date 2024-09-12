from pydantic import BaseModel, PositiveFloat, EmailStr, validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    nome: str
    descricao: str
    preco: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr


    class Config:
        from_attributes = True

class ProductGet(ProductBase):
    id: int
    created_at: datetime
    updated: bool | None = None
    update_date: datetime | None

    class Config:
        from_attributes = True

class ProductUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    preco: Optional[PositiveFloat] = None
    categoria: Optional[str] = None
    email_fornecedor: Optional[EmailStr] = None

