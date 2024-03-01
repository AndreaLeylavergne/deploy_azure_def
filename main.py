from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
import pickle
from keras.models import load_model

# Create the FastAPI app
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": " Hello, beautifull World 3.11"}



