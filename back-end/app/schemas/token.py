from typing import Optional
from pydantic import BaseModel

class TokenOutput(BaseModel):
    access_token: str
    refresh_token: str
