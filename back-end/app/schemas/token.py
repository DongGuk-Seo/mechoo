from typing import Optional
from pydantic import BaseModel

class TokenBase(BaseModel):
    refresh_token: str

class TokenOutput(TokenBase):
    access_token: str

class AuthInput(TokenBase):
    user_id: int
    location: str