from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    username: str
    is_active: bool = True
    created_at: datetime = datetime.now()

class UserCreate(UserBase):
    email: str
    username: str
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class User(UserBase):
    id: int

    class Config:
        orm_mode = True