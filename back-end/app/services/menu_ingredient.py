from crud import menu_ingredient
from models.menu import MenuIngredient
from fastapi import Response
from api.deps import SessionDep
from schemas.menu_ingredient import MenuIngredientCreate
from services.menu import MenuService
from services.ingredient import IngredientService
from utils.exceptions import exception_400_client_error, exception_404_not_found

class MenuIngredientService:
    def __init__(self) -> None:
        self.menu_service = MenuService()
        self.ingredient_service = IngredientService()
        pass

    async def create_menu_ingredient(self, db: SessionDep, obj_in: MenuIngredientCreate) -> MenuIngredient:

        # Valid
        await self.menu_service.get_by_id(db=db, id=obj_in.menu_id)
        await self.ingredient_service.get_by_id(db=db, id=obj_in.ingredient_id)

        menu_ingredient_model = menu_ingredient.create(db=db, obj_in=obj_in)
        return menu_ingredient_model
    
    async def delete_menu_ingredient(self, db: SessionDep, id: int) -> Response:
        result = menu_ingredient.delete(db=db, id=id)
        if result:
            return Response("메뉴 재료를 성공적으로 삭제했습니다.")
        raise exception_404_not_found("존재하지 않는 메뉴 재료입니다.")