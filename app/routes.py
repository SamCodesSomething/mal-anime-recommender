from http.client import HTTPException
from fastapi import FastAPI, Query, APIRouter, Request
from fastapi.responses import HTMLResponse
from app.mal_api import search_anime_by_title, get_client_id
router = APIRouter()
CLIENT_ID = get_client_id()

@router.get("/search-text", summary="Search anime by title", response_description="List of anime matching the search title", response_class=HTMLResponse)
async def search_anime_text(
    request: Request,
    title: str = Query(..., min_length=1, description="Title of the anime to search")
):
    if not CLIENT_ID:
        raise Exception("CLIENT_ID is not set") #raises exception if client id isn't working

    results = search_anime_by_title(title, CLIENT_ID)

    if not results or "data" not in results:
        raise HTTPException(404, "No Results Found") #raises 404 if nothing found

    lines = []
    for anime in results["data"]:
        node = anime["node"]
        title = node.get("title", "N/A")
        mean = node.get("mean", "N/A")
        genres = ', '.join(g["name"] for g in node.get("genres", []))
        lines.append(f"Title: {title}\nRating: {mean}\nGenres: {genres}\n")

    return "\n".join(lines)
