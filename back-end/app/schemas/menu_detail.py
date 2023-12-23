from typing import Optional
from pydantic import BaseModel

class MenuDetailBase(BaseModel):
    menu_id: int
    sweet_level: int
    hot_level: int
    sour_level: int
    oil_level: int
    include_meat: bool
    include_veget: bool
    food_type: str
    country: str