from sqlalchemy.orm import Session
from app.models import Factor
from app.schemas import FactorCreate,FactorUpdate


def create_factor(db:Session , factor:FactorCreate):
    db_factor = Factor(customer_id = factor.customer_id , total = factor.total) #jalalidate=factor.jalalidate
    db.add(db_factor)
    db.commit()
    db.refresh(db_factor)
    return db_factor

def read_all_factors(db:Session): 
    return db.query(Factor).all()

def read_factor_by_id(db:Session, id:int):
    return db.get(Factor , id)

def update_factor(db:Session , updated_factor:FactorUpdate):
    db_factor = db.get(Factor,updated_factor.id)
    if not db_factor:
        return False
    db_factor.customer_id = updated_factor.customer_id 
    # db_factor.jalalidate = updated_factor.jalalidate
    db_factor.total = updated_factor.total
    db.commit()
    db.refresh(db_factor)
    return db_factor

def delete_all_factors(db:Session):
    deleted = db.query(Factor).delete()
    db.commit()
    return deleted

def delete_factor_by_id(db:Session , id:int ):
    deleted = db.get(Factor, id)
    if not deleted:
        return False
    db.delete(deleted)
    db.commit() 
    return True

def search_factor(db:Session ,fid:int ,cid:int ,minprice,maxprice,mindate,maxdate):
    query = db.query(Factor)
    if fid !=None :
        query = query.filter(Factor.id == fid)
    if cid != None :
        query = query.filter(Factor.customer_id == cid)
    if minprice !=None :
        query = query.filter(Factor.total >= minprice )
    if maxprice != None :
        query = query.filter(Factor.total <= maxprice)
    if mindate !='' :
        query = query.filter(Factor.date >= mindate)
    if maxdate != '' :
        query = query.filter(Factor.date <= maxdate)
    return query.all()