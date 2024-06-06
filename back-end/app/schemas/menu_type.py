from typing import Optional
from pydantic import BaseModel

class MenuTypeBase(BaseModel):
    id: int

class MenuTypeCreateRequest(BaseModel):
    type_name: str
    
class MenuTypeUpdateRequest(MenuTypeBase):
    type_name: str