from typing import Optional, List

from sqlalchemy.orm import Session
from crud.base import CRUDBase
from utils.exceptions import exception_400_client_error
from models.menu import MenuType
from schemas.menu_type import MenuTypeCreateRequest, MenuTypeUpdateRequest

class CRUDMenuType(CRUDBase[MenuType, MenuTypeCreateRequest, MenuTypeUpdateRequest]):
    def get_by_id(self, db: Session, id: int) -> Optional[MenuType]:
        return db.query(MenuType).filter(MenuType.id == id).first()

    def create(self, db: Session, obj_in: MenuTypeCreateRequest) -> MenuType:
        db_obj = MenuType(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: MenuType, obj_in: MenuTypeUpdateRequest) -> MenuType:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

menu_Type = CRUDMenuType(MenuType)