from fastapi import FastAPI, Query, APIRouter
from fastapi.responses import JSONResponse
from app.mal_api import search_anime_by_title, get_client_id
app = FastAPI()

router = APIRouter()
CLIENT_ID = get_client_id()

@router.get("/search")
async def search_anime(title: str = Query(..., min_length=1)):
    results = search_anime_by_title(title, CLIENT_ID)

    if not results or "data" not in results:
        return JSONResponse(content={"error": "No results found"}, status_code=404)

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
