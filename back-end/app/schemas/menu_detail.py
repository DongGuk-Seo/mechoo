from typing import Optional
from pydantic import BaseModel

class MenuDetailBase(BaseModel):
    menu_id: int
    menu_type_id: int
    menu_country_id: int

class MenuDetailCreate(MenuDetailBase):
    sweet_level: int
    sour_level: int
    oil_level: int
    spicy_level: int
    is_cold_food: bool
    include_meat: bool
    include_veget: bool
    
    
class MenuDetailUpdate(MenuDetailBase):
    sweet_level: Optional[int]
    sour_level: Optional[int]
    oil_level: Optional[int]
    spicy_level: Optional[int]
    is_cold_food: Optional[bool]
    include_meat: Optional[bool]
    include_veget: Optional[bool]
    
class MenuDetailOutput(MenuDetailCreate):
    id: int