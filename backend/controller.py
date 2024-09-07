from sqlalchemy.orm import Session
from . import schemas
from . import models

def get_products(db:Session):
    return db.query(models.ProductModel).all()

def get_product(db:Session, produto_id: int):
    return db.query(models.ProductModel).filter(models.ProductModel.id == produto_id).first()


def create_product(db: Session, produto:schemas.ProductBase):
    db_products = models.ProductModel(**produto.model_dump())
    db.add(db_products)
    db.commit()
    db.refresh(db_products)
    return db_products

def update_product(db: Session,produto_id: int, produto: schemas.ProductUpdate):
    db_product = db.query(models.ProductModel).filter(models.ProductModel.id == produto_id).first()

    if db_product is None:
        return None
    if produto.nome is not None:
        db_product.nome = produto.nome
    if produto.descricao is not None:
        db_product.descricao = produto.descricao
    if produto.preco is not None:
        db_product.preco = produto.preco
    if produto.categoria is not None:
        db_product.categoria = produto.categoria
    if produto.email_fornecedor is not None:
        db_product.email_fornecedor = produto.email_fornecedor
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, produto_id: int):
    db_product = db.query(models.ProductModel).filter(models.ProductModel.id == produto_id).first()
    if db_product is None:
        return None
    db.delete(db_product)
    db.commit()
    return db_product