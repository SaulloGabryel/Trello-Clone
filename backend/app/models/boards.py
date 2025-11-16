from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from database import Base

class Board(Base):
    __tablename__ = 'boards'

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(40), nullable = False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable= False)