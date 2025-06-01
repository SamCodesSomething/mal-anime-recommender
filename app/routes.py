from http.client import HTTPException
from fastapi import FastAPI, Query, APIRouter
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.mal_api import search_anime_by_title, get_client_id
router = APIRouter()
CLIENT_ID = get_client_id()

templates = Jinja2Templates(directory="app/templates")
@router.get("/search-ui", summary="Search anime by title", response_description="List of anime matching the search title", response_class=HTMLResponse)
async def search_anime_ui(title: str = Query(..., min_length=1, description="Title of the anime to search")):
    if not CLIENT_ID:
        raise Exception("CLIENT_ID is not set")
    results = search_anime_by_title(title, CLIENT_ID)

    if not results or "data" not in results:
        raise HTTPException(404, "No Results Found")

    formatted = []
    for anime in results["data"]:
        node = anime["node"]
        formatted.append({
            "title": node.get("title", "N/A"),
            "mean": node.get("mean", "N/A"),
            "genres": [g["name"] for g in node.get("genres", [])],
            "image": node.get("main_picture", {}).get("medium", "N/A")
        })

    return {"results": formatted}
