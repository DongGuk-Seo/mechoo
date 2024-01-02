from typing import Optional, List

from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.menu import MenuRecipe
from schemas.recipe import RecipeCreate, RecipeUpdate

class CRUDRecipe(CRUDBase[MenuRecipe, RecipeCreate, RecipeUpdate]):
    def get_recipe_by_menu_id(self, db: Session, menu_id: int) -> Optional[MenuRecipe]:
        return db.query(MenuRecipe).filter(MenuRecipe.menu_id ==  menu_id).first()
    
    def get_all_recipe(self, db: Session) -> List[MenuRecipe]:
        return db.query(MenuRecipe).all()
    
    def create(self, db: Session, obj_in: RecipeCreate) -> MenuRecipe:
        db_obj = MenuRecipe(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: MenuRecipe, obj_in: RecipeUpdate) -> MenuRecipe:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

recipe = CRUDRecipe(MenuRecipe)