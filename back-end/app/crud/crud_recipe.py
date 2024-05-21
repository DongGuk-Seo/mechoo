from typing import Optional, List

from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.menu import Recipe
from schemas.recipe import RecipeCreate, RecipeUpdate

class CRUDRecipe(CRUDBase[Recipe, RecipeCreate, RecipeUpdate]):
    def get_recipe_by_menu_id(self, db: Session, menu_id: int) -> Optional[Recipe]:
        return db.query(Recipe).filter(Recipe.menu_id ==  menu_id).first()
    
    def get_all_recipe(self, db: Session) -> List[Recipe]:
        return db.query(Recipe).all()
    
    def create(self, db: Session, obj_in: RecipeCreate) -> Recipe:
        db_obj = Recipe(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: Recipe, obj_in: RecipeUpdate) -> Recipe:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)
    
    def delete(self, db: Session, id: int) -> bool:
        obj = db.query(Recipe).filter(Recipe.id == id).first()
        if obj:
            db.delete(obj)
            db.commit()
            return True
        return False
recipe = CRUDRecipe(Recipe)