from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from database import Base
from .boards import Board

class List(Base):
    __tablename__ = 'lists'

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(40), nullable = False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable= False)
    board_id = Column(ForeignKey(Board.id), nullable= False)