from typing import Optional, Union, List

from fastapi import APIRouter
from api.deps import SessionDep
from schemas.ingredient import IngredientCreate, IngredientUpdate, IngredientOutput
from services.ingredient import IngredientService

router = APIRouter()

@router.post("")
async def create_ingredient(db: SessionDep, obj_in: IngredientCreate) -> IngredientOutput:
    ingredient_service = IngredientService()
    ingredient_model = await ingredient_service.create_ingredient(db=db, obj_in=obj_in)
    return IngredientOutput(**ingredient_model.__dict__)

@router.get("")
async def get_ingredient_all(db: SessionDep) -> List[IngredientOutput]:
    ingredient_service = IngredientService()
    ingredient_models = await ingredient_service.get_all_ingredient(db=db)
    return [IngredientOutput(**ingredient_model.__dict__) for ingredient_model in ingredient_models]

@router.get("/")
async def get_ingredient_by_ingredient_kind(db: SessionDep, kind: str) -> List[IngredientOutput]:
    ingredient_service = IngredientService()
    ingredient_models = await ingredient_service.get_all_ingredient_by_kind(db=db, kind=kind)
    return [IngredientOutput(**ingredient_model.__dict__) for ingredient_model in ingredient_models]