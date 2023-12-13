from datetime import datetime, timedelta
from typing import Any, Union, Optional

from jose import jwt
from passlib.context import CryptContext

from core.config import settings
from schemas.token import TokenOutput

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"

def valid_token(exp: datetime) -> bool:
    return datetime.utcnow() <= exp

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

def decode_token(token: str) -> Optional[dict]:
    decoded_token = jwt.decode(token=token, key=settings.SECRET_KEY, algorithms=ALGORITHM,)
    if valid_token(decoded_token["exp"]):
        return decoded_token


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)