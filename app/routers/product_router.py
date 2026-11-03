from fastapi import APIRouter,HTTPException,Depends,status
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import product_crud
from typing import List
from app.schemas import ProductCreate,ProductUpdate,ProductOut

router = APIRouter(prefix='/products',tags=['Products'])

@router.post('/CreateProduct/',response_model=ProductOut)
def create_product(product:ProductCreate,db:Session = Depends(get_db)):
    new_product = product_crud.create_product(db, product) #or (db, product=product)
    return new_product

@router.get('/ReadAllProducts/',response_model=List[ProductOut])
def read_products(db:Session = Depends(get_db)):
    products = product_crud.get_all_products(db)
    return products or []

@router.get('/ReadProductById/{product_id}/',response_model=ProductOut)
def read_product_by_id(product_id:int,db:Session = Depends(get_db)):
    product = product_crud.get_product_by_id(db,product_id=product_id) #or (db, product_id)
    if not product:
        raise HTTPException(status_code=404,detail='product not found')
    return product 

@router.put('/UpdateProduct/',response_model=ProductOut)
def update_product(updated_product :ProductUpdate, db:Session = Depends(get_db)):  # inja bayad ProductCreate bezaram ya ProductUpdate ? batavajoh be file schemas tu update ke id dare? aslan bayad id tu update bezaram?
    db_product = product_crud.update_product(db,updated_product=updated_product) 
    if not db_product:
        raise HTTPException(status_code=404,detail='product not found')
    return db_product

@router.delete('/DeleteAllProducts/')
def delete_all_products(db:Session = Depends(get_db)):
    count = product_crud.delete_all_products(db)
    return {'detail':f'{count} products deleted'}

@router.delete('/DeleteProductbyId/{product_id}/')
def delete_product_by_id(product_id:int , db:Session = Depends(get_db)):
    deleted = product_crud.delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404,detail='product not found')
    return {'detail':'product deleted successfully'}
