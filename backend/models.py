#representacao do banco de dados
from sqlalchemy import Column, Integer, String, DateTime, Select, Boolean, Float
from sqlalchemy.sql import func
from .database import Base

class ProductModel(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String, index=True)
    preco = Column(Float, index=True)
    categoria = Column(String, index=True)
    email_fornecedor = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), index=True)

