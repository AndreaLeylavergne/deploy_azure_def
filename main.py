from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tensorflow as tf

# Create the FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": " Hello, beautifull World 3.11"}



