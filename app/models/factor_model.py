from sqlalchemy import Column, Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime,date

class Factor(Base):
    __tablename__ = 'factors' 

    id = Column(Integer,primary_key = True, index = True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    date = Column(String, default=date.today())  #datetime.utcnow
    total = Column(Integer,default = 0)
    # jalalidate = Column(String, default=None)
 
    customer = relationship('Customer',back_populates='factors')
    items = relationship('FactorItem',back_populates='factor')
    