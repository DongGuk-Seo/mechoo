import secrets, os
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    # Will be changed
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # A Week : 60 minutes * 24 hours * 7 days
    ACCESS_TOKEN_EXPIRE_TIME: int = 60 * 24 * 7
    # SERVER_NAME: str
    # SERVER_HOST: AnyHttpUrl
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    PROJECT_NAME: str = "MeChoo"
    # SENTRY_DSN: Optional[HttpUrl] = None
    
    # @validator("SENTRY_DSN", pre=True)
    # def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
    #     if len(v) == 0:
    #         return None
    #     return v

    def set_db_url(self) -> str:
        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")
        server = os.getenv("POSTGRES_SERVER")
        database = os.getenv("POSTGRES_DB")
        return f'postgresql://{user}:{password}@{server}/{database}'
    
    # POSTGRES_SERVER: str
    # POSTGRES_DB: str
    # POSTGRES_DB_USER: str
    # POSTGRES_DB_PASSWORD: str
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    # @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    # def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
    #     if isinstance(v, str):
    #         return v
    #     return PostgresDsn.build(
    #         scheme="postgresql+psycopg",
    #         user=values.get("POSTGRES_USER"),
    #         password=values.get("POSTGRES_PASSWORD"),
    #         host=values.get("POSTGRES_SERVER"),
    #         path=f"/{values.get('POSTGRES_DB') or ''}",
    #     )
    
        
    class Config:
        case_sensitive = True

settings = Settings()