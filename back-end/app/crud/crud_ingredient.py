from typing import Optional, List

from sqlalchemy.orm import Session
from crud.base import CRUDBase
from core.utils import exception_400_already_exist
from models.menu import Ingredient
from schemas.ingredient import IngredientCreate, IngredientUpdate

class CRUDIngredient(CRUDBase[Ingredient, IngredientCreate, IngredientUpdate]):
    def get_ingredient_all(self, db: Session) -> List[Ingredient]:
        return db.query(Ingredient).all()
    
    def get_ingredient_all_by_type(self, db: Session, type:str) -> List[Ingredient]:
        return db.query(Ingredient).filter(Ingredient.type == type).all()
    
    def get_ingredient_by_name(self, db: Session, name:str) -> Optional[Ingredient]:
        return db.query(Ingredient).filter(Ingredient.name == name).first()

    def create(self, db: Session, obj_in: IngredientCreate) -> Ingredient:
        db_obj = Ingredient(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: Ingredient, obj_in: IngredientUpdate) -> Ingredient:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

ingredient = CRUDIngredient(Ingredient)