from fastapi.testclient import TestClient

from working import app

client = TestClient(app)

def test_repos():
    response_repos = client.get("/user/Obrepal/repos")
    assert response_repos.status_code == 200

def test_bytes():
   response_bytes = client.get("/user/Obrepal/bytes")
   assert response_bytes.status_code == 200
