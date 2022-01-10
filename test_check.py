from fastapi.testclient import TestClient

from Repo_info import app

client = TestClient(app)


def test_repos():
    response_repos = client.get("/user/Obrepal/repos")
    if response_repos.status_code == 500:
        assert response_repos.json() == {'detail': 'Item not found'}
    else:
        assert response_repos.status_code == 200

def test_stars():
   response_stars = client.get("/user/Obrepal/stars")
   if response_stars.status_code == 500:
    assert response_stars.json() == {'detail': 'Item not found'}
   else: 
    assert response_stars.status_code == 200

def test_stars_quantity():
   response_stars = client.get("/user/Obrepal/stars")
   if response_stars.status_code == 500:
    assert response_stars.json() == {'detail': 'Item not found'}
   else: 
    assert   response_stars.json() == {"Total_stars": 0}

    #{"Bytes in given language":{"Python":[2,35184],"C":[1,17047],"Makefile":[1,192],"Shell":[1,102],"MATLAB":[1,22632],"Java":[1,34921]}}
