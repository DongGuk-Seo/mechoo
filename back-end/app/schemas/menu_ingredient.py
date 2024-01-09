from typing import Optional, List
from pydantic import BaseModel

class MenuBase(BaseModel):
    menu_id: int

class MenuIngredientRequest(MenuBase):
    ingredient_list: List[int]

class MenuIngredientCreate(MenuBase):
    ingredient_id: int
    
class MenuIngredientUpdate(MenuBase):
    ingredient_id: Optional[int]
    
class MenuIngredientOutput(MenuBase):
    ingredient_list: List[int]