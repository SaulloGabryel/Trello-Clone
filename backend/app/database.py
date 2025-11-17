from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
from datetime import datetime


Base = declarative_base()

engine = create_engine("mysql+pymysql://root:%23Digimon1230@localhost/trello_clone")
