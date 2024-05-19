from typing import Optional
from pydantic import BaseModel

class IngredientBase(BaseModel):
    id: int

class IngredientCreate(IngredientBase):
    name: str
    type: str

class IngredientUpdate(IngredientBase):
    type: Optional[str]

class IngredientOutput(IngredientCreate):
    id: int