from sqlalchemy.orm import Session
from app.models import Customer
from app.schemas import CustomerCreate,CustomerUpdate,CustomerOut

def create_customer(db: Session , customer: CustomerCreate):
    db_customer = Customer(username = customer.username, pic = customer.pic)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_all_customers(db: Session):  
    return db.query(Customer).all() 

def get_customer_by_id(db: Session, customer_id:int):
    return db.get(Customer, customer_id)

def update_customer(db:Session, updated_customer: CustomerUpdate):
    db_customer = db.get(Customer,updated_customer.id)
    if db_customer is None:
        return None
    db_customer.username = updated_customer.username
    db_customer.pic = updated_customer.pic
    db.commit()
    db.refresh(db_customer)
    return db_customer

def delete_all_customers(db:Session):
    deleted = db.query(Customer).delete()
    db.commit()
    return deleted

def delete_customer(db:Session , customer_id:int):
    customer = db.get(Customer, customer_id)
    if not customer:
        return False
    db.delete(customer)
    db.commit()
    return True

def search_customers(db: Session, id:int, username:str):   #get_customer_by_name_or_id
    query = db.query(Customer)
    if username !='' :
        query = query.filter(Customer.username.like(f'%{username}%'))
    if id != None :
        query = query.filter(Customer.id == id)
    return query.all()
