from pydantic import BaseModel

class FactorItemBase(BaseModel):
    fid : int
    pid : int
    no :int
    price : int
    my_sum :int

class FactorItemCreate(FactorItemBase):
    pass

class FactorItemUpdate(FactorItemBase):
    id : int

class FactorItemOut(FactorItemBase): 
    id : int
    # my_sum :int  
    class config:
        from_attributes = True