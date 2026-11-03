from fastapi import APIRouter,HTTPException,Depends,status
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import factor_item_crud
from typing import List
from app.schemas import FactorItemCreate,FactorItemUpdate,FactorItemOut

router = APIRouter(prefix='/factoritems',tags=['Factor Items'])

@router.post('/CreateFactorItem/',response_model=FactorItemOut)
def create_factoritem(factoritem:FactorItemCreate,db:Session = Depends(get_db)):
    new_factoritem = factor_item_crud.create_factor_item(db, factoritem)
    return new_factoritem

# @router.post('/CreateFactorItem/')
# def create_factoritem(factoritems: list[FactorItemCreate],db: Session = Depends(get_db)):
#     result = []
#     for item in factoritems:
#         new_factoritem = factor_item_crud.create_factor_item(db, item)
#         result.append(new_factoritem)
#     return result


@router.get('/ReadAllFactorItems/',response_model=List[FactorItemOut])
def read_factoritems(db:Session = Depends(get_db)):
    factoritems = factor_item_crud.read_all_factor_items(db)
    return factoritems or []
 
@router.get('/ReadFactorItemById/{factoritem_id}/',response_model=FactorItemOut)
def read_factoritem_by_id(factoritem_id:int,db:Session = Depends(get_db)):
    factoritem = factor_item_crud.read_factoritem_by_id(db, factoritem_id)
    if not factoritem:
        raise HTTPException(status_code=404,detail='factoritem not found')
    return factoritem

@router.get('/ReadFactorItemByFid/{fid}/',response_model=List[FactorItemOut])
def read_factoritem_by_fid(fid:int,db:Session = Depends(get_db)):
    factoritems = factor_item_crud.read_factoritem_by_fid(db, fid)
    # if not factoritems:
    #     raise HTTPException(status_code=404,detail='factoritem not found')
    return factoritems or []

@router.put('/UpdateFactorItem/',response_model=FactorItemOut)
def update_factoritem(updated_factoritem :FactorItemUpdate, db:Session = Depends(get_db)):
    db_factoritem = factor_item_crud.update_factoritem(db, updated_factoritem) 
    if not db_factoritem:
        raise HTTPException(status_code=404,detail='factoritem not found')
    return db_factoritem

@router.delete('/DeleteAllFactorItems/')
def delete_all_factoritems(db:Session = Depends(get_db)):
    count = factor_item_crud.delete_all_factoritems(db)
    return {'detail':f'{count} factoritems deleted'}

@router.delete('/DeleteFactorItemById/{factoritem_id}/')
def delete_factoritem_by_id(factoritem_id:int , db:Session = Depends(get_db)):
    deleted = factor_item_crud.delete_factoritem_by_id(db, factoritem_id)
    if not deleted:
        raise HTTPException(status_code=404,detail='factoritem not found')
    return {'detail':'factoritem deleted successfully'}

@router.delete('/DeleteFactorItemByFid/{fid}/')
def delete_factoritem_by_fid(fid:int , db:Session = Depends(get_db)):
    deleted = factor_item_crud.delete_factoritem_by_fid(db, fid)
    if not deleted:
        raise HTTPException(status_code=404,detail='factoritem not found')
    return {'detail':'factoritem deleted successfully'}
