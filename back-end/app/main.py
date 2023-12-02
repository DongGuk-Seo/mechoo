from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.config import settings
from models import user
from db.engine import engine

user.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=settings.API_V1_STR, docs_url=f'{settings.API_V1_STR}/docs'
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# app.include_router()