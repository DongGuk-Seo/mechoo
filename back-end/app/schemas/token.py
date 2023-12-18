from typing import Optional
from pydantic import BaseModel

class TokenBase(BaseModel):
    refresh_token: str

class TokenOutput(TokenBase):
    access_token: str

class TokenInput(TokenBase):
    user_id: int
    location: str

class TokenUpdate(TokenBase):
    is_expired: bool