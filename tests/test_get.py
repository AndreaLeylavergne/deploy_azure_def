from fastapi.testclient import TestClient
from main import app 
#import sys
#sys.path.append(r'C:\Users\andre\deploy_azure_def')  

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": " Hello, World 3.11"}
