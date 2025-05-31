from app.mal_api import search_anime_by_title, get_anime_recommendations
import os
import pytest
from dotenv import load_dotenv
load_dotenv()

fake_client_id = "invalid_id"



@pytest.fixture(scope="module")
def client_id():
    cid = os.getenv("MAL_CLIENT_ID")
    if not cid:
        pytest.skip("MAL_CLIENT_ID environment variable not set, skipping tests that require it")
    return cid

def test_env():
    print("MAL_CLIENT_ID:", os.getenv("MAL_CLIENT_ID"))
    assert os.getenv("MAL_CLIENT_ID") is not None

def test_valid_search(client_id):
    data = search_anime_by_title("Naruto", client_id)
    assert data is not None
    assert "data" in data
    assert isinstance(data["data"], list)

def test_invalid_client_id():
    data = search_anime_by_title("Naruto", fake_client_id)
    assert data is None  # should handle bad client ID gracefully

def test_empty_title(client_id):
    data = search_anime_by_title("", client_id)
    assert data is None

def test_invalid_title(client_id):
    data = search_anime_by_title("faewfeawfaewfawefaewffegaew", client_id)
    assert data is not None
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) == 0  # Should return an empty list

def test_valid_recommendations(client_id):
    # Use a known anime ID
    data = get_anime_recommendations(20, client_id)
    assert data is not None
    assert "data" in data
    assert isinstance(data["data"], list)

def test_invalid_anime_id(client_id):
    data = get_anime_recommendations(9999999, client_id)
    assert data is None  # should return None