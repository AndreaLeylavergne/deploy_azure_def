import pytest
from fastapi.testclient import TestClient
from main import app 

# Définition du fixture pour initialiser l'application avec le TestClient
@pytest.fixture(scope="session")
def test_client():
    # Utilisation du TestClient pour créer une instance client de votre application FastAPI
    with TestClient(app) as client:
        yield client

# Fonction de test pour vérifier le sentiment positif
def test_positive_sentiment(test_client):
    request_data = {"text": "I really love this company with all my heart"}
    response = test_client.post("/predict", json=request_data)
    assert response.status_code == 200
    assert response.json()["sentiment"] == "Positive"

# Fonction de test pour vérifier le sentiment négatif
def test_negative_sentiment(test_client):
    request_data = {"text": "I hate airlines. @Delta has a mechanical issue that delays a flight for over two hours but no refund possible."}
    response = test_client.post("/predict", json=request_data)
    assert response.status_code == 200
    assert response.json()["sentiment"] == "Negative"
