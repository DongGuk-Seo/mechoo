from typing import Optional, List

from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.menu import MenuIngredient
from schemas.menu_ingredient import MenuIngredientCreate, MenuIngredientUpdate, MenuIngredientOutput

class CRUDMenuIngredient(CRUDBase[MenuIngredient, MenuIngredientCreate, MenuIngredientUpdate]):
    def get_ingredient_by_menu_id(self, db: Session, id: int) -> List[MenuIngredient]:
        return db.query(MenuIngredient).filter(MenuIngredient.id == id).all()

    def create(self, db: Session, obj_in: MenuIngredientCreate) -> MenuIngredient:
        db_obj = MenuIngredient(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    # TODO : Many to Many update Logic
    def update(self, db: Session, db_obj: MenuIngredient, obj_in: MenuIngredientUpdate) -> MenuIngredient:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

menu_ingredient = CRUDMenuIngredient(MenuIngredient)