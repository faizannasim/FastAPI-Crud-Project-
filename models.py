from sqlalchemy import Column,String,Integer
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    email = Column(String(255),unique=True)
    password = Column(String(255))
    description  = Column(String(255))