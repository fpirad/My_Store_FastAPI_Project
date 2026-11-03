from pydantic import BaseModel
from typing import List
from .factor_schema import FactorItemOut

class ProductBase(BaseModel):
    name : str
    price : int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    id : int

class ProductOut(ProductBase):
    id : int
    items: List[FactorItemOut]
    class config:
        from_attributes = True
 