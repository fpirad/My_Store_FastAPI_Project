from sqlalchemy.orm import Session
from app.models import FactorItem
from app.schemas import FactorItemCreate,FactorItemUpdate,FactorItemOut

def create_factor_item(db:Session , factoritem:FactorItemCreate):
    db_factoritem = FactorItem(fid = factoritem.fid , pid = factoritem.pid , no = factoritem.no , price = factoritem.price, my_sum = factoritem.my_sum)
    db.add(db_factoritem)
    db.commit()
    db.refresh(db_factoritem)
    return db_factoritem

def read_all_factor_items(db:Session):
    return db.query(FactorItem).all()

def read_factoritem_by_id(db:Session, id:int):
    return db.get(FactorItem , id)

def read_factoritem_by_fid(db:Session , fid:int):
    return db.query(FactorItem).filter(FactorItem.fid == fid).all()

def update_factoritem(db:Session , updated_factoritem:FactorItemUpdate):
    db_factoritem = db.get(FactorItem,updated_factoritem.id)
    if not db_factoritem:
        return False
    db_factoritem.fid = updated_factoritem.fid
    db_factoritem.pid = updated_factoritem.pid
    db_factoritem.no = updated_factoritem.no
    db_factoritem.price = updated_factoritem.price
    db_factoritem.my_sum = updated_factoritem.my_sum
    db.commit()
    db.refresh(db_factoritem)
    return db_factoritem

def delete_all_factoritems(db:Session):
    deleted = db.query(FactorItem).delete()
    db.commit()
    return deleted

def delete_factoritem_by_id(db:Session , id:int ):
    deleted = db.get(FactorItem, id)
    if not deleted:
        return False
    db.delete(deleted)
    db.commit()
    return True

def delete_factoritem_by_fid(db:Session , fid:int ):
    deleted = db.query(FactorItem).filter(FactorItem.fid == fid).all()
    if not deleted:
        return False
    for i in deleted:
        db.delete(i)
    db.commit()
    return True
