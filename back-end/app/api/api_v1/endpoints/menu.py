from typing import Optional, Union, List

from fastapi import APIRouter, Request, HTTPException, Response
from api.deps import SessionDep
from schemas.menu import MenuCreate, MenuUpdate, MenuOutput
from schemas.menu_detail import MenuDetailCreate, MenuDetailOutput, MenuDetailUpdate
from schemas.menu_recipe import MenuRecipeCreate, MenuRecipeUpdate, MenuRecipeOutput
from schemas.menu_image import MenuImageCreate, MenuImageUpdate, MenuImageOutput
from schemas.menu_ingredient import MenuIngredientCreateRequest, MenuIngredientCreate, MenuIngredientUpdate, MenuIngredientOutput
from services.menu import MenuService
from services.menu_detail import MenuDetailService
from services.menu_recipe import MenuRecipeService
from services.menu_image import MenuImageService
from services.menu_ingredient import MenuIngredientService
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

@router.post("/recipe")
async def create_menu_recipe(db: SessionDep, obj_in: MenuRecipeCreate) -> MenuRecipeOutput:
    menu_recipe_service = MenuRecipeService()
    menu_recipe_model = await menu_recipe_service.create_menu_recipe(db=db, obj_in=obj_in)
    return MenuRecipeOutput(**menu_recipe_model.__dict__)

@router.put("/recipe")
async def update_menu_recipe(db: SessionDep, obj_in: MenuRecipeUpdate) -> MenuRecipeOutput:
    menu_recipe_service = MenuRecipeService()
    menu_recipe_model = await menu_recipe_service.update_menu_recipe(db=db, obj_in=obj_in)
    return MenuRecipeOutput(**menu_recipe_model.__dict__)

@router.get("/recipe/")
async def get_menu_recipe_by_menu_id(db: SessionDep, menu_id: int) -> MenuRecipeOutput:
    menu_recipe_service = MenuRecipeService()
    menu_recipe_model = await menu_recipe_service.get_menu_recipe_by_menu_id(db=db, menu_id=menu_id)
    return MenuRecipeOutput(**menu_recipe_model.__dict__)

@router.post("/image")
async def create_menu_image(db: SessionDep, obj_in: MenuImageCreate) -> MenuImageOutput:
    menu_image_service = MenuImageService()
    menu_image_model = await menu_image_service.create_menu_image(db=db, obj_in=obj_in)
    return MenuImageOutput(**menu_image_model.__dict__)

@router.post("/image/")
async def get_menu_image_by_menu_id(db: SessionDep, menu_id: int) -> MenuImageOutput:
    menu_image_service = MenuImageService()
    menu_image_model = await menu_image_service.get_menu_image_by_menu_id(db=db, menu_id=menu_id)
    return MenuImageOutput(**menu_image_model.__dict__)

@router.post("/ingredient")
async def create_menu_ingredient(db: SessionDep, obj_in: MenuIngredientCreateRequest) -> MenuIngredientOutput:
    menu_ingredient_service = MenuIngredientService()
    output = MenuIngredientOutput(menu_id=-1, ingredient_list=[])
    # TODO : Chunk Create
    for ingredient_id in obj_in.ingredient_id_list:
        menu_ingredient_model = await menu_ingredient_service.create_menu_ingredient(db=db, obj_in=MenuIngredientCreate(menu_id=obj_in.menu_id, ingredient_id=ingredient_id))
        output.menu_id = menu_ingredient_model.menu_id
        output.ingredient_list.append(menu_ingredient_model.ingredient_id)
    return output