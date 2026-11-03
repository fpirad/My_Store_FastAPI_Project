from sqlalchemy import Column, Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class FactorItem(Base):
    __tablename__ = 'factor_items' 

    id = Column(Integer,primary_key = True, index = True)
    fid = Column(Integer, ForeignKey('factors.id'))
    pid = Column(Integer, ForeignKey('products.id'))
    no = Column(Integer,default = 0)
    price = Column(Integer,default = 0)
    my_sum = Column(Integer,default = 0)

    factor = relationship('Factor',back_populates='items')
    product = relationship('Product',back_populates='items') 