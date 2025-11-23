from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
from datetime import datetime
from dotenv import load_dotenv
import os


Base = declarative_base()
load_dotenv()

database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url)
