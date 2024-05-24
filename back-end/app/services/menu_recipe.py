from crud import menu_recipe
from fastapi import Response
from typing import Optional, List
from api.deps import SessionDep
from models.menu import MenuRecipe
from schemas.menu_recipe import MenuRecipeCreate, MenuRecipeUpdate
from utils.exceptions import exception_400_client_error, exception_404_not_found

class MenuRecipeService:

    async def get_menu_recipe_by_menu_id(self, db: SessionDep, menu_id: int) -> Optional[MenuRecipe]:
        return menu_recipe.get_menu_recipe_by_menu_id(db=db, menu_id=menu_id)

    async def create_menu_recipe(self, db: SessionDep, obj_in: MenuRecipeCreate) -> MenuRecipe:
        if menu_recipe.get_menu_recipe_by_menu_id(db=db, menu_id=obj_in.menu_id):
            raise exception_400_client_error("이미 존재하는 레시피입니다.")
        recipe_model = menu_recipe.create(db=db, obj_in=obj_in)
        return recipe_model
    
    async def update_menu_recipe(self, db: SessionDep, obj_in: MenuRecipeUpdate) -> MenuRecipe:
        recipe_model = menu_recipe.get_menu_recipe_by_menu_id(db=db, menu_id=obj_in.menu_id)
        if recipe_model:
            updated_recipe_model = menu_recipe.update(db=db, db_obj=recipe_model, obj_in=obj_in)
            return updated_recipe_model
        raise exception_404_not_found("존재하지 않는 레시피입니다.")