from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    username: str
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class User(UserBase):
    username: str
    id: int

    class Config:
        orm_mode = True

class UserSignin(UserBase):
    password: str