from crud import recipe
from fastapi import Response
from typing import Optional, List
from api.deps import SessionDep
from models.menu import Recipe
from schemas.recipe import RecipeCreate, RecipeUpdate
from utils.exceptions import exception_400_client_error, exception_404_not_found

class RecipeService:
    async def get_recipe_by_menu_id(self, db: SessionDep, menu_id: int) -> Optional[Recipe]:
        return recipe.get_recipe_by_menu_id(db=db, menu_id=menu_id)
    
    async def is_existed_recipe_by_menu_id(self, db: SessionDep, menu_id: int) -> Optional[Recipe]:
        return recipe.get_recipe_by_menu_id(db=db, menu_id=menu_id)

    async def create_recipe(self, db: SessionDep, obj_in: RecipeCreate) -> Recipe:
        if await self.is_existed_recipe_by_menu_id(db=db, menu_id=obj_in.menu_id):
            raise exception_400_client_error("이미 존재하는 레시피입니다.")
        recipe_model = recipe.create(db=db, obj_in=obj_in)
        return recipe_model
    
    async def update_recipe(self, db: SessionDep, obj_in: RecipeUpdate) -> Recipe:
        recipe_model = recipe.get_recipe_by_menu_id(db=db, menu_id=obj_in.menu_id)
        if recipe_model:
            updated_recipe_model = recipe.update(db=db, db_obj=recipe_model, obj_in=obj_in)
            return updated_recipe_model
        raise exception_404_not_found("존재하지 않는 레시피입니다.")
    
    async def delete_recipe(self, db: SessionDep, id: int) -> Response:
        recipe_model = recipe.delete(db=db, id=id)
        if recipe_model:
            return Response("레시피를 성공적으로 삭제했습니다.")
        raise exception_404_not_found("존재하지 않는 레시피입니다.")