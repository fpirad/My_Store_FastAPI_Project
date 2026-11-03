from fastapi import APIRouter,HTTPException,Depends,status
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import customer_crud
from typing import List
from app.schemas import CustomerCreate,CustomerUpdate,CustomerOut

router = APIRouter(prefix='/customers',tags=['Customers'])

@router.post('/CreateCustomer/',response_model=CustomerOut)
def create_customer(customer:CustomerCreate,db:Session = Depends(get_db)):
    new_customer = customer_crud.create_customer(db,customer)
    return new_customer 

@router.get('/ReadAllCustomers/',response_model=List[CustomerOut])
def read_customers(db:Session = Depends(get_db)):
    customers = customer_crud.get_all_customers(db)
    return customers or []

@router.get('/ReadCustomerById/{customer_id}/',response_model=CustomerOut)
def read_customer_by_id(customer_id:int,db:Session = Depends(get_db)):
    customer = customer_crud.get_customer_by_id(db,customer_id)
    if not customer:
        raise HTTPException(status_code=404,detail='customer not found')
    return customer

@router.put('/UpdateCustomer/',response_model=CustomerOut)
def update_customer(updated_customer :CustomerUpdate, db:Session = Depends(get_db)):
    db_customer = customer_crud.update_customer(db,updated_customer) #???? chera yeja tu crud_customer update ba get neveshte yeja ba query neveshte , customer id ham behesh dade ostad?
    if not db_customer:
        raise HTTPException(status_code=404,detail='customer not found')
    return db_customer

@router.delete('/DeleteAllCustomers/')
def delete_all_customers(db:Session = Depends(get_db)):
    count = customer_crud.delete_all_customers(db)
    return {'detail':f'{count} customers deleted'}

@router.delete('/DeleteCustomerbyId/{customer_id}/')
def delete_customer_by_id(customer_id:int , db:Session = Depends(get_db)):
    deleted = customer_crud.delete_customer(db,customer_id)
    if not deleted:
        raise HTTPException(status_code=404,detail='customer not found')
    return {'detail':'customer deleted successfully'}

@router.get('/SearchCustomer/',response_model=List[CustomerOut])
def search_customer(id:int=None , username:str='' ,db:Session = Depends(get_db)):
    customer = customer_crud.search_customers(db,id,username)
    if not customer:
        raise HTTPException(status_code=404,detail='customer not found')
    return customer