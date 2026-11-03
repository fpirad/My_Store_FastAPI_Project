from sqlalchemy import Column, Integer,String,Boolean
from sqlalchemy.orm import relationship
from app.database import Base
 
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer,primary_key = True, index = True)
    name = Column(String, nullable= False)
    price = Column(Integer,nullable= False,default = 0)
    # is_active = Column(Boolean, default=True)

    items = relationship('FactorItem',back_populates='product')  
  