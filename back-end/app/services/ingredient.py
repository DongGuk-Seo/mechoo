from crud import ingredient
from fastapi import Response
from typing import Optional, List
from api.deps import SessionDep
from models.menu import Ingredient
from schemas.ingredient import IngredientCreate, IngredientUpdate
from utils.exceptions import exception_400_client_error, exception_404_not_found

class IngredientService:
    async def get_all_ingredient(self, db: SessionDep) -> List[Ingredient]:
        return ingredient.get_ingredient_all(db=db)
    
    async def get_all_ingredient_by_type(self, db: SessionDep, ingredient_type: str) -> List[Ingredient]:
        return ingredient.get_ingredient_all_by_type(db=db, ingredient_type=ingredient_type)
    
    async def is_existed_ingredient_by_name(self, db: SessionDep, name: str) -> Optional[Ingredient]:
        return ingredient.get_ingredient_by_name(db=db, name=name)

    async def create_ingredient(self, db: SessionDep, obj_in: IngredientCreate) -> Ingredient:
        if await self.is_existed_ingredient_by_name(db=db, name=obj_in.name):
            raise exception_400_client_error("이미 존재하는 재료입니다.")
        ingredient_model = ingredient.create(db=db, obj_in=obj_in)
        return ingredient_model
    
    async def update_ingredient(self, db: SessionDep, obj_in: IngredientUpdate) -> Ingredient:
        ingredient_model = ingredient.get_ingredient_by_id(db=db, id=obj_in.id)
        if ingredient_model:
            updated_ingredient_model = ingredient.update(db=db, db_obj=ingredient_model, obj_in=obj_in)
            return updated_ingredient_model
        raise exception_404_not_found("존재하지 않는 재료입니다.")
    
    async def delete_ingredient(self, db: SessionDep, id: int) -> Response:
        ingredient_model = ingredient.delete(db=db, id=id)
        if ingredient_model:
            return Response("재료를 성공적으로 삭제했습니다.")
        raise exception_404_not_found("존재하지 않는 재료입니다.")