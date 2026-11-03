from pydantic import BaseModel
from typing import List
from datetime import datetime
from .factor_item_schema import FactorItemOut

class FactorBase(BaseModel):
    customer_id : int
    # jalalidate :str
    total : int

class FactorCreate(FactorBase):
    pass
 
class FactorUpdate(FactorBase):
    id : int  

class FactorOut(FactorBase):
    id : int
    date :datetime
    total : int
    items : List[FactorItemOut]
    class config:
        from_attributes = True 