from typing import Optional, List

from sqlalchemy.orm import Session
from crud.base import CRUDBase
from core.utils import exception_400_already_exist
from models.menu import MenuImage
from schemas.menu_image import MenuImageCreate, MenuImageUpdate, MenuImageOutput

class CRUDMenuImage(CRUDBase[MenuImage, MenuImageCreate, MenuImageUpdate]):
    def get_menu_image_by_menu_id(self, db: Session, menu_id: int) -> Optional[MenuImage]:
        return db.query(MenuImage).filter(MenuImage.menu_id == menu_id).first()

    def create(self, db: Session, obj_in: MenuImageCreate) -> MenuImage:
        db_obj = MenuImage(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: MenuImage, obj_in: MenuImageUpdate) -> MenuImage:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)
    
    def valid_is_exist(self, db:Session, menu_id:int) -> None:
        if self.get_menu_image_by_menu_id(db=db, menu_id=menu_id):
            raise exception_400_already_exist("이미 존재하는 이미지입니다.")

menu_image = CRUDMenuImage(MenuImage)