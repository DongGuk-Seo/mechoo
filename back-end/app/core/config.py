import secrets, os
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, EmailStr, HttpUrl, PostgresDsn, validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    
    API_V1_STR: str = "/api"
    # JWT_SECRET_KEY: str = secrets.token_urlsafe(32)
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "")
    # 60 minutes * 24 hours * 3 days
    ACCESS_TOKEN_EXPIRE_TIME: int = 60 * 24 * 3
    REFRESH_TOKEN_EXPIRE_TIME: int = 60 * 24 * 7
    # SERVER_NAME: str = "Mechoo"
    # SERVER_HOST: AnyHttpUrl
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    
    PROJECT_NAME: str = "MeChoo"
    # SENTRY_DSN: Optional[HttpUrl] = None
    
    # @validator("SENTRY_DSN", pre=True)
    # def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
    #     if len(v) == 0:
    #         return None
    #     return v

    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "")
    
settings = Settings()