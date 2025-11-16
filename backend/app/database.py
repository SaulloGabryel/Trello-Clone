from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
import os
from datetime import datetime

engine = create_engine("mysql+pymysql://root:%23Digimon1230@localhost/trello_clone")

Base = declarative_base