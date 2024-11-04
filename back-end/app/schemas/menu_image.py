from typing import Optional
from pydantic import BaseModel

class MenuImageBase(BaseModel):
    menu_id: int

class MenuImageCreate(MenuImageBase):
    image_url: str
    
class MenuImageUpdate(MenuImageBase):
    image_url: Optional[str]
    
class MenuImageOutput(MenuImageBase):
    id: int