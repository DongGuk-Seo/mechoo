from typing import Optional, List
from pydantic import BaseModel

class MenuIngredientBase(BaseModel):
    menu_id: int

class MenuIngredientCreate(MenuIngredientBase):
    ingredient_list: List[int]
    
class MenuIngredientUpdate(MenuIngredientBase):
    ingredient_list: List[int]
    
class MenuIngredientOutput(MenuIngredientBase):
    ingredient_list: List[int]