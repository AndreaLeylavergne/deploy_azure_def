from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": " Hello, World"}



