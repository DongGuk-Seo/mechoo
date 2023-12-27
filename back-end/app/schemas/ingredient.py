from typing import Optional
from pydantic import BaseModel

class IngredientBase(BaseModel):
    name: str

class IngredientCreate(IngredientBase):
    type: str

class IngredientUpdate(BaseModel):
    name: Optional[str]
    type: Optional[str]

class IngredientOutput(IngredientCreate):
    id: int