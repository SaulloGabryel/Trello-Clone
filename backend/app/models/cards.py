from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from database import Base
from .lists import List

class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(40), nullable = False)
    description = Column(String(30), nullable= True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable= False)
    list_id = Column(ForeignKey(List.id),  nullable= False)
    order = Column(Integer, nullable= False)

