from database import Base, engine
from models.boards import Board
from models.lists import Lists
from models.cards import Cards
from models.user import User

Base.metadata.create_all(bind=engine)
print("Tables created!")
