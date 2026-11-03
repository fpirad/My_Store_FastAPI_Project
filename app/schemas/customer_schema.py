from pydantic import BaseModel
from typing import List
from .factor_schema import FactorOut 

class CustomerBase(BaseModel):
    username : str
    pic : str

class CustomerCreate(CustomerBase):
    # password : str
    pass

class CustomerUpdate(CustomerBase):
    id : int
    # password : str

class CustomerOut(CustomerBase): 
    id : int
    factors: List[FactorOut]
    class config:
        from_attributes = True
