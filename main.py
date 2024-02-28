from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import pickle
import nltk
from nltk.corpus import stopwords
import re
from unidecode import unidecode
import uvicorn

# Create the FastAPI app
app = FastAPI()

# Padding des séquences pour avoir la même longueur
max_length = 40

def transformer_texte_en_sequence(textes, tokenizer, max_length):
    sequences = [tokenizer.texts_to_sequences([text])[0] for text in textes]
    sequences_pad = pad_sequences(sequences, maxlen=max_length)
    return sequences_pad

class InputData(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(input_data: InputData):
    text = input_data.text
    text_data = transformer_texte_en_sequence([text], tokenizer, max_length)
    sentiment_pred = model.predict(text_data)
    sentiment_score = sentiment_pred[0][0]
    sentiment_label = "Positive" if sentiment_score >= 0.5 else "Negative"

    return {"sentiment": sentiment_label, "score": float(sentiment_score)}

@app.get("/")
def read_root():
    return {"message": " Hello, World"}



