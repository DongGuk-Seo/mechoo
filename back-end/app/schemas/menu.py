from typing import Optional
from pydantic import BaseModel

class MenuBase(BaseModel):
    name: str

class MenuCreate(MenuBase):
    summary: str

class MenuUpdate(BaseModel):
    id: int
    summary: Optional[str]

class MenuOutput(MenuBase):
    id: int