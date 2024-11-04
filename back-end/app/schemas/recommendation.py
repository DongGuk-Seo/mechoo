from typing import Optional, List
from pydantic import BaseModel

class RecommendationBase(BaseModel):
    pass

class RecommendByFlavorRequest(BaseModel):
    sweet_level: int
    sour_level: int
    oil_level: int
    spicy_level: int
    is_cold_food: Optional[bool]
    include_meat: Optional[bool]
    include_veget: Optional[bool]

class RecommendByIngredientRequest(BaseModel):
    ingredient_list: List[str]

class RecommendByCountryRequest(BaseModel):
    name: str

class RecommendByMenuTypeRequest(BaseModel):
    name: str