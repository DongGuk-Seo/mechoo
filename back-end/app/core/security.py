from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext

from core.config import settings
from schemas.token import TokenOutput

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"


def create_token(subject: Union[str, Any]) -> TokenOutput:
    access_expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_TIME)
    refresh_expire = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_TIME)
    access_to_encode = {"exp": access_expire, "sub": str(subject)}
    refresh_to_encode = {"exp": refresh_expire, "sub": str(subject)}
    tokens = TokenOutput(
        access_token=jwt.encode(access_to_encode, settings.SECRET_KEY, algorithm=ALGORITHM),
        refresh_token=jwt.encode(refresh_to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    )
    return tokens


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)