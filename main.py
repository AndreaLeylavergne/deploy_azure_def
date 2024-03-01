from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
import pickle
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer

# Définir le chemin du modèle

model_path = 'glove_model_lstm'

# Charger le modèle sauvegardé
#loaded_model = tf.keras.models.load_model(model_path)

ml_models = {}  # Définir ml_models comme un dictionnaire vide
model = None  # Initialiser model à None

# Fonction pour charger le modèle de manière asynchrone
async def load_ml_model():
    global model  # Utiliser la variable model définie en dehors de la fonction
    try:
        model = load_model(model_path)
    except OSError:
        raise HTTPException(status_code=500, detail="Impossible de charger le modèle")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model asynchronously
    await load_ml_model()
    ml_models["glove_model_lstm"] = model  # Utiliser la variable model mise à jour ici
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


# Create the FastAPI app
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": " Hello, beautifull World 3.11"}



