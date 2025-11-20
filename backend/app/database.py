from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
from datetime import datetime
from ..env import database_url

Base = declarative_base()

engine = create_engine(database_url)
