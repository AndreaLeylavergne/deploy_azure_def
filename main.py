from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer

# Create the FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": " Hello, beautifull world 3.11"}



