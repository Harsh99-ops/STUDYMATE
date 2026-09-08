from fastapi import FastAPI

from app.database.connection import engine, Base
from app.models.space import Space
from app.api.routes.spaces import router as spaces_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="STUDYMATE",
    description="AI-powered Study and Research Intelligence Platform",
    version="1.0.0"
)


app.include_router(spaces_router)


@app.get("/")
def root():
    return {
        "message": "STUDYMATE API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }