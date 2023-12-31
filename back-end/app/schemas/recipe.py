from typing import Optional
from pydantic import BaseModel

class RecipeBase(BaseModel):
    menu_id: int

class RecipeCreate(RecipeBase):
    recipe: str
    source_link: str

class RecipeUpdate(RecipeBase):
    recipe: Optional[str]
    source_link: Optional[str]

class RecipeOutput(RecipeCreate):
    id: int