from fastapi.testclient import TestClient

from working import app

client = TestClient(app)

def test_repos():
    response_repos = client.get("/user/Obrepal/repos")
    assert response_repos.status_code == 200

#def test_repos():
   # response_repos = client.get("/user/Obrepal/bytes")
    #assert response_repos.status_code == 200
