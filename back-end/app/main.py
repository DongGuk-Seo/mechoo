from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.config import settings
from db.engine import engine
from models import user
from api.api_v1.api import api_router

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

app.include_router(api_router, prefix=settings.API_V1_STR)