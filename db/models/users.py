from enum import unique
from pickle import TRUE
from re import S
from database import Base
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Column

class User(Base):
    __tablename__ = 'user'
    id =  Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    url_image = Column(String)
