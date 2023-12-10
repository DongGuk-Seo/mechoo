from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UsernameBase(BaseModel):
    username: str

class UserCreate(UserBase):
    username: str
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserSignin(UserBase):
    password: str

class UserOutput(UserBase):
    username: str
    id: int

    class Config:
        orm_mode = True