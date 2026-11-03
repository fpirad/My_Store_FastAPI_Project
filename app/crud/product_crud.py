from sqlalchemy.orm import Session
from app.models import Product
from app.schemas import ProductCreate,ProductUpdate,ProductOut

def create_product(db: Session , product: ProductCreate):
    db_product = Product(name = product.name, price = product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
 
def get_all_products(db: Session):
    return db.query(Product).all()

def get_product_by_name(db: Session, name:str):
    return db.query(Product).filter(Product.name ==name).first()

def get_product_by_id(db: Session, product_id:int):
    return db.get(Product, product_id)
 
def update_product(db:Session, updated_product: ProductUpdate):
    db_product = db.get(Product,updated_product.id)
    if db_product is None:
        return None
    db_product.name = updated_product.name
    db_product.price = updated_product.price
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_all_products(db:Session):
    deleted = db.query(Product).delete()
    db.commit()
    return deleted

def delete_product(db:Session , product_id:int):
    product = db.get(Product, product_id)
    if not product:
        return False
    db.delete(product)
    db.commit()
    return True