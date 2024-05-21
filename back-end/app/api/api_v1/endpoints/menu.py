from typing import Optional, Union, List

from fastapi import APIRouter, Request, HTTPException, Response
from crud import menu, menu_detail, ingredient, recipe, menu_image, menu_ingredient
from api.deps import SessionDep
from models.menu import Menu, Ingredient
from schemas.menu import MenuCreate, MenuUpdate, MenuOutput
from schemas.menu_detail import MenuDetailCreate, MenuDetailOutput, MenuDetailUpdate
from schemas.ingredient import IngredientCreate, IngredientUpdate, IngredientOutput
from schemas.recipe import RecipeCreate, RecipeOutput
from schemas.menu_image import MenuImageCreate, MenuImageUpdate, MenuImageOutput
from schemas.menu_ingredient import MenuIngredientRequest, MenuIngredientCreate, MenuIngredientUpdate, MenuIngredientOutput
from services.menu import MenuService
from services.menu_detail import MenuDetailService
from services.ingredient import IngredientService
from services.recipe import RecipeService
from utils.exceptions import exception_400_client_error, exception_404_not_found

router = APIRouter()

@router.post("")
async def create_menu(db: SessionDep, obj_in: MenuCreate) -> MenuOutput:
    menu_service = MenuService()
    menu_model = await menu_service.create_menu(db=db, obj_in=obj_in)
    return MenuOutput(**menu_model.__dict__)

@router.put("")
async def update_menu(db: SessionDep, obj_in: MenuUpdate) -> MenuOutput:
    menu_service = MenuService()
    updated_menu_model = await menu_service.update_menu(db=db, obj_in=obj_in)
    return MenuOutput(**updated_menu_model.__dict__)

@router.delete("/{id}")
async def delete_menu(db: SessionDep, id: int) -> Response:
    menu_service = MenuService()
    return await menu_service.delete_menu(db=db, id=id)

@router.post("/detail")
async def create_menu_detail(db: SessionDep, obj_in: MenuDetailCreate) -> MenuDetailOutput:
    menu_detail_service = MenuDetailService()
    menu_detail_model = await menu_detail_service.create_menu_detail(db=db, obj_in=obj_in)
    return MenuDetailOutput(**menu_detail_model.__dict__)

@router.put("/detail")
async def update_menu_detail(db: SessionDep, obj_in: MenuDetailUpdate) -> MenuDetailOutput:
    menu_detail_service = MenuDetailService()
    menu_detail_model = await menu_detail_service.update_menu_detail(db=db, obj_in=obj_in)
    return MenuDetailOutput(**menu_detail_model.__dict__)

@router.delete("/detail/{id}")
async def delete_menu_detail(db: SessionDep, id: int) -> Response:
    menu_detail_service = MenuDetailService()
    return await menu_detail_service.delete_menu_detail(db=db, id=id)
    
@router.post("/ingredient")
async def create_ingredient(db: SessionDep, obj_in: IngredientCreate) -> IngredientOutput:
    ingredient_service = IngredientService()
    ingredient_model = await ingredient_service.create_ingredient(db=db, obj_in=obj_in)
    return IngredientOutput(**ingredient_model.__dict__)

@router.get("/ingredient")
async def get_ingredient_all(db: SessionDep) -> List[IngredientOutput]:
    ingredient_service = IngredientService()
    ingredient_models = await ingredient_service.get_all_ingredient(db=db)
    return [IngredientOutput(**ingredient_model.__dict__) for ingredient_model in ingredient_models]

@router.get("/ingredient/")
async def get_ingredient_by_ingredient_type(db: SessionDep, ingredient_type: str) -> List[IngredientOutput]:
    ingredient_service = IngredientService()
    ingredient_models = await ingredient_service.get_all_ingredient_by_type(db=db, ingredient_type=ingredient_type)
    return [IngredientOutput(**ingredient_model.__dict__) for ingredient_model in ingredient_models]

@router.post("/recipe")
async def create_recipe(db: SessionDep, obj_in: RecipeCreate) -> RecipeOutput:
    recipe_service = RecipeService()
    recipe_model = await recipe_service.create_recipe(db=db, obj_in=obj_in)
    return RecipeOutput(**recipe_model.__dict__)

@router.get("/recipe/")
async def get_recipe_by_menu_id(db: SessionDep, menu_id:int) -> RecipeOutput:
    recipe_service = RecipeService()
    recipe_model = await recipe_service.get_recipe_by_menu_id(db=db, menu_id=menu_id)
    return RecipeOutput(**recipe_model.__dict__)

@router.post("/image")
async def create_menu_image(session: SessionDep, menu_image_in: MenuImageCreate) -> MenuImageOutput:
    if menu_image.get_menu_image_by_menu_id(db=session, menu_id=menu_image_in.menu_id):
        raise exception_400_client_error("이미 존재하는 이미지입니다.")
    menu_image_model = menu_image.create(db=session, obj_in=menu_image_in)
    return MenuImageOutput(**menu_image_model.__dict__)

@router.post("/menu/ingredient")
async def create_menu_ingredient(session: SessionDep, menu_ingredient_in: MenuIngredientRequest) -> MenuIngredientOutput:
    menu_id = menu_ingredient_in.menu_id
    ingredient_list = []
    for ingredient_id in menu_ingredient_in.ingredient_list:
        menu_ingredient_model = menu_ingredient.create(db=session, obj_in=MenuIngredientCreate(
            menu_id= menu_id,
            ingredient_id=ingredient_id
            ))
        ingredient_list.append(menu_ingredient_model.ingredient_id)
    return MenuIngredientOutput(menu_id=menu_id, ingredient_list=ingredient_list)