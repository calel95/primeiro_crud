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





def delete_product(db: Session, produto_id: int):
    db_product = db.query(models.ProductModel).filter(models.ProductModel.id == produto_id).first()
    if db_product is None:
        return None
    db.delete(db_product)
    db.commit()
    return db_product