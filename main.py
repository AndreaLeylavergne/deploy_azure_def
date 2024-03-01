from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
import pickle
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer


# Create the FastAPI app
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": " Hello, beautifull World 3.11"}



