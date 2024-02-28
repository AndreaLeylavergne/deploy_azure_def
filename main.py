from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import uvicorn

# Create the FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": " Hello, World"}



