#representacao do banco de dados
from sqlalchemy import Column, Integer, String, DateTime, Select, Boolean, Float
from sqlalchemy.sql import func
from database import Base

class ProductModel(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(Float)
    categoria = Column(String)
    email_fornecedor = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())

