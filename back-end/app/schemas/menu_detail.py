from typing import Optional
from pydantic import BaseModel

class MenuDetailBase(BaseModel):
    menu_id: int

class MenuDetailCreate(MenuDetailBase):
    sweet_level: int
    hot_level: int
    sour_level: int
    oil_level: int
    include_meat: bool
    include_veget: bool
    food_type: str
    country: str
    
class MenuDetailUpdate(MenuDetailBase):
    sweet_level: Optional[int]
    hot_level: Optional[int]
    sour_level: Optional[int]
    oil_level: Optional[int]
    include_meat: Optional[bool]
    include_veget: Optional[bool]
    food_type: Optional[str]
    country: Optional[str]
    
class MenuDetailOutput(MenuDetailCreate):
    id: int