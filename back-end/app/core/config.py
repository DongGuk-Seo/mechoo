import secrets
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    # Will be changed
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # A Week : 60 minutes * 24 hours * 7 days
    ACCESS_TOKEN_EXPIRE_TIME: int = 60 * 24 * 7
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    ALLOW_CORS_ORIGIN: List[AnyHttpUrl] = []


    POSTGRES_SERVER: str
    POSTGRES_DB: str
    POSTGRES_DB_USER: str
    POSTGRES_DB_PASSWORD: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

settings = Settings()