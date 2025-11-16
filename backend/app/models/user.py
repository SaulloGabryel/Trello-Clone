from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer,primary_key= True, index= True)
    username = Column(String(15), nullable= False, unique= True)
    email = Column(String(100), unique = True)
    hashed_password = Column(String(20), nullable= False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable = False)

