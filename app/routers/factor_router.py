from fastapi import APIRouter,HTTPException,Depends,status
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import factor_crud
from typing import List 
from app.schemas import FactorCreate,FactorUpdate,FactorOut

router = APIRouter(prefix='/factors',tags=['Factors'])

@router.post('/CreateFactor/',response_model=FactorOut)
def create_factor(factor:FactorCreate,db:Session = Depends(get_db)):
    new_factor = factor_crud.create_factor(db,factor)
    return new_factor

@router.get('/ReadAllFactors/',response_model=List[FactorOut])
def read_factors(db:Session = Depends(get_db)):
    factors = factor_crud.read_all_factors(db)
    return factors or []

@router.get('/ReadFactorById/{factor_id}/',response_model=FactorOut)
def read_factor_by_id(factor_id:int,db:Session = Depends(get_db)):
    factor = factor_crud.read_factor_by_id(db,id=factor_id) # or (db,factor_id)
    if not factor:
        raise HTTPException(status_code=404,detail='factor not found')
    return factor

@router.put('/UpdateFactor/',response_model=FactorOut) 
def update_factor(updated_factor:FactorUpdate, db:Session = Depends(get_db)):
    db_factor = factor_crud.update_factor(db,updated_factor) 
    if not db_factor:
        raise HTTPException(status_code=404,detail='factor not found')
    return db_factor

@router.delete('/DeleteAllFactors/')
def delete_all_factors(db:Session = Depends(get_db)):
    count = factor_crud.delete_all_factors(db)
    return {'detail':f'{count} factors deleted'}

@router.delete('/DeleteFactorById/{factor_id}/')
def delete_factor_by_id(factor_id:int , db:Session = Depends(get_db)):
    deleted = factor_crud.delete_factor_by_id(db,factor_id)
    if not deleted:
        raise HTTPException(status_code=404,detail='factor not found')
    return {'detail':'factor deleted successfully'}

@router.get('/SearchFactor/',response_model=List[FactorOut])
def search_factor(fid:int=None , cid:int=None ,minprice:int=None ,maxprice:int=None, mindate='' , maxdate='' ,db:Session = Depends(get_db)):
    factor = factor_crud.search_factor(db,fid,cid,minprice,maxprice,mindate,maxdate)
    if not factor:
        raise HTTPException(status_code=404,detail='factor not found')
    return factor


