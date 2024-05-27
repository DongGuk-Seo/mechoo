from typing import Optional
from pydantic import BaseModel

class IngredientBase(BaseModel):
    kind: str

class IngredientCreate(IngredientBase):
    name: str
    
class IngredientUpdate(IngredientBase):
    id: int

class IngredientOutput(IngredientCreate):
    id: int