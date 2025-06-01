from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_search_anime_success():
    response = client.get("/search?title=Naruto")
    assert response.status_code == 200
    assert "results" in response.json()

def test_search_anime_no_title():
    response = client.get("/search")  # no title param
    assert response.status_code == 422  # validation error from FastAPI

def test_search_anime_no_result():
    response = client.get("42718947912")
    assert response.status_code == 404