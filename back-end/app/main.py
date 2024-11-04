from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.config import settings
from db.engine import engine
from models import user, token, menu
from api.api_v1.api import api_router
import uvicorn

user.Base.metadata.create_all(bind=engine)
token.Base.metadata.create_all(bind=engine)
menu.Base.metadata.create_all(bind=engine)

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

log_config = uvicorn.config.LOGGING_CONFIG
log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True, log_config=log_config)