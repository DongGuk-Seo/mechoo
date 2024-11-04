from crud import menu_image
from fastapi import Response
from typing import Optional, List
from api.deps import SessionDep
from models.menu import MenuImage
from schemas.menu_image import MenuImageCreate, MenuImageUpdate
from utils.exceptions import exception_400_client_error, exception_404_not_found

class MenuImageService:

    async def get_by_menu_id(self, db: SessionDep, menu_id: int) -> Optional[MenuImage]:
        return menu_image.get_by_menu_id(db=db, menu_id=menu_id)

    async def create_menu_image(self, db: SessionDep, obj_in: MenuImageCreate) -> MenuImage:
        if self.get_by_menu_id(db=db, menu_id=obj_in.menu_id):
            raise exception_400_client_error("이미 존재하는 이미지입니다.")
        menu_image_model = menu_image.create(db=db, obj_in=obj_in)
        return menu_image_model
    
    async def update_menu_image(self, db: SessionDep, obj_in: MenuImageUpdate) -> MenuImage:
        menu_image_model = await self.get_by_menu_id(db=db, menu_id=obj_in.menu_id)
        if menu_image_model:
            updated_menu_image_model = menu_image.update(db=db, db_obj=menu_image_model, obj_in=obj_in)
            return updated_menu_image_model
        raise exception_404_not_found("존재하지 않는 재료입니다.")