from fastapi.testclient import TestClient
from app.main import app

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

def test_search_anime_cowboy_bebop(): #
    response = client.get("/search?title=Cowboy Bebop")
    assert response.status_code == 200
    