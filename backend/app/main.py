import sqlalchemy
import os
import dotenv
from fastapi import FastAPI
import pydantic

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

