from typing import Optional, List

from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.menu import MenuDetail
from schemas.menu_detail import MenuDetailBase, MenuDetailCreate, MenuDetailUpdate

class CRUDMenuDetail(CRUDBase[MenuDetail, MenuDetailCreate, MenuDetailUpdate]):
    def get_menu_by_menu_id(self, db: Session, menu_id: int) -> Optional[MenuDetail]:
        return db.query(MenuDetail).filter(MenuDetail.menu_id == menu_id).first()

    def create(self, db: Session, obj_in: MenuDetailCreate) -> MenuDetail:
        db_obj = MenuDetail(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: MenuDetail, obj_in: MenuDetailUpdate) -> MenuDetail:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

menu_detail = CRUDMenuDetail(MenuDetail)