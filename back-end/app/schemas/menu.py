from typing import Optional
from pydantic import BaseModel

class MenuBase(BaseModel):
    name: str

class MenuCreate(MenuBase):
    summary: str

class MenuUpdate(MenuCreate):
    id: int

class MenuOutput(MenuBase):
    id: int