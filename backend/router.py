from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import database, schemas, controller
from typing import List

router = APIRouter()

@router.get("/produtos/", response_model=List[schemas.ProductGet])
def read_all_products(db: Session = Depends(database.get_db)):
    products = controller.get_products(db)
    return products

@router.get("/produtos/{produto_id}", response_model=schemas.ProductGet)
def read_one_product(produto_id: int, db: Session = Depends(database.get_db)):
    db_product = controller.get_product(db=db, produto_id=produto_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Produto com o id {produto_id} não encontrado")
    return db_product

@router.post("/produtos", response_model=schemas.ProductBase)
def create_product(produto: schemas.ProductBase ,db: Session = Depends(database.get_db)):
    db_product = controller.create_product(db=db,produto=produto)
    return db_product

@router.delete("/produtos/{produto_id}", response_model=schemas.ProductGet)
def delete_product(produto_id: int, db: Session = Depends(database.get_db)):
    db_product = controller.delete_product(db=db,produto_id=produto_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Produto com o id {produto_id} não encontrado")
    return db_product

@router.put("/produtos/{produto_id}",response_model=schemas.ProductGet)
def update_products(produto_id: int, produto: schemas.ProductUpdate, db: Session = Depends(database.get_db)):
    db_product = controller.update_product(db=db, produto_id=produto_id, produto=produto)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Produto com o id {produto_id} não encontrado")
    return db_product