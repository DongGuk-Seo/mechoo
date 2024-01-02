from typing import Optional, Union, List

from fastapi import APIRouter, Request, HTTPException, Response
from crud import menu, menu_detail, ingredient, recipe
from api.deps import SessionDep
from models.menu import Menu, Ingredient
from schemas.menu import MenuCreate, MenuUpdate, MenuOutput
from schemas.menu_detail import MenuDetailCreate, MenuDetailOutput, MenuDetailUpdate
from schemas.ingredient import IngredientCreate, IngredientUpdate, IngredientOutput
from schemas.recipe import RecipeCreate, RecipeOutput
from core.utils import exception_400_already_exist, exception_404_not_found

router = APIRouter()

@router.post("")
async def create_menu(session: SessionDep, menu_in: MenuCreate) -> MenuOutput:
    menu_model = menu.create(db=session, obj_in=menu_in)
    return MenuOutput(**menu_model.__dict__)

@router.put("/summary")
async def update_summary(session: SessionDep, menu_in: MenuUpdate) -> MenuOutput:
    menu_model = menu.get_menu_by_id(db=session, id=menu_in.id)
    if menu_model:
        new_menu = menu.update(db=session, db_obj=menu_model, obj_in= menu_in)
        return MenuOutput(**new_menu.__dict__)
    raise exception_404_not_found("존재하지 않는 메뉴 입니다.")

@router.post("/detail")
async def create_menu_detail(session: SessionDep, menu_detail_in: MenuDetailCreate) -> MenuDetailOutput:
    if menu.get_menu_by_id(db=session,id=menu_detail_in.menu_id):
        menu_detail.valid_is_exist(db=session,menu_id=menu_detail_in.menu_id)
        menu_detail_model = menu_detail.create(db=session, obj_in=menu_detail_in)
        return MenuDetailOutput(**menu_detail_model.__dict__) 
    raise exception_404_not_found("존재하지 않는 메뉴 입니다.")

@router.put("/detail")
async def update_menu_detail(session: SessionDep, menu_detail_in: MenuDetailUpdate) -> MenuDetailOutput:
    if menu.get_menu_by_id(db=session,id=menu_detail_in.menu_id):
        menu_detail_model = menu_detail.get_menu_detail_by_menu_id(db=session, menu_id=menu_detail_in.menu_id)
        if menu_detail_model:
            new_menu_detail = menu_detail.update(db=session,db_obj=menu_detail_model, obj_in=menu_detail_in)
            return MenuDetailOutput(**new_menu_detail.__dict__)
        raise exception_404_not_found("존재하지 않는 메뉴 세부정보 입니다.")
    raise exception_404_not_found("존재하지 않는 메뉴 입니다.")
    
@router.post("/ingredient")
async def create_ingredient(session: SessionDep, ingredient_in: IngredientCreate) -> IngredientOutput:
    if ingredient.get_ingredient_by_name(db=session,name=ingredient_in.name):
        raise exception_400_already_exist("이미 존재하는 재료입니다.")
    ingredient_model = ingredient.create(db=session, obj_in=ingredient_in)
    return IngredientOutput(**ingredient_model.__dict__)

@router.get("/ingredient")
async def get_ingredient_all(session: SessionDep) -> List[IngredientOutput]:
    data = ingredient.get_ingredient_all(db=session)
    print(data)
    return [IngredientOutput(**i.__dict__) for i in data]

@router.get("/ingredient/{type}")
async def get_ingredient_by_type(session: SessionDep, type: str) -> List[IngredientOutput]:
    data = ingredient.get_ingredient_all_by_type(db=session,type=type)
    return [IngredientOutput(**datum.__dict__) for datum in data]

@router.post("/recipe")
async def create_recipe(session: SessionDep, recipe_in: RecipeCreate) -> RecipeOutput:
    if recipe.get_recipe_by_menu_id(db=session, menu_id=recipe_in.menu_id):
        raise exception_400_already_exist("이미 존재하는 재료입니다.")
    recipe_model = recipe.create(db=session, obj_in=recipe_in)
    return RecipeOutput(**recipe_model.__dict__)