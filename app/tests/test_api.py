from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_review_endpoint():
    response = client.post("/token")
    assert response.status_code == 200
    token = response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/api/review/", json={"content": "This product is very good."}, headers=headers)
    
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "positive"
