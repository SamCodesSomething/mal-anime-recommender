from fastapi import FastAPI
from app.routes import router
app = FastAPI(
    swagger_ui_parameters={"defaultModelsExpandDepth": -2},
    title="MyAnimeList Anime Search API",
    description="An API to search for anime using the official MyAnimeList API.",
    version="1.0.0",
    contact={
        "name": "Sam Hopkins",
        "url": "https://github.com/SamCodesSomething",
        "email": "SamHopkinsBusiness@gmail.com",
    }

)
app.include_router(router)