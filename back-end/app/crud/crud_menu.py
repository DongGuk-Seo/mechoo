from typing import Optional, List

from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.menu import Menu
from schemas.menu import MenuCreate, MenuUpdate

class CRUDMenu(CRUDBase[Menu, MenuCreate, MenuUpdate]):
    def get_all_menu(self, db: Session, name: str) -> List[Menu]:
        return db.query(Menu).filter(Menu.name == name).all()
    
    def get_menu_by_name(self, db: Session, name: str) -> Optional[Menu]:
        return db.query(Menu).filter(Menu.name == name).first()
    
    def get_menu_by_id(self, db: Session, id: int) -> Optional[Menu]:
        return db.query(Menu).filter(Menu.id == id).first()

    def create(self, db: Session, obj_in: MenuCreate) -> Menu:
        db_obj = Menu(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: Menu, obj_in: MenuUpdate) -> Menu:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

menu = CRUDMenu(Menu)