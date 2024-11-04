from typing import Optional
from pydantic import BaseModel

class MenuRecipeBase(BaseModel):
    menu_id: int

class MenuRecipeCreate(MenuRecipeBase):
    recipe: str
    source_link: str

class MenuRecipeUpdate(MenuRecipeBase):
    recipe: Optional[str]
    source_link: Optional[str]

class MenuRecipeOutput(MenuRecipeCreate):
    id: int