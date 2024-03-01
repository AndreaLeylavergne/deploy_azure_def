from fastapi import FastAPI
from pydantic import BaseModel

# Create the FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": " Hello, beautifull World 3.11"}



