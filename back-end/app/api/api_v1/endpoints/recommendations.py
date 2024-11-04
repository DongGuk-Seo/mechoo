from fastapi import APIRouter, Request
from api.deps import SessionDep
from services.recommendation import RecommendationService
from schemas.recommendation import RecommendByFlavorRequest, RecommendByIngredientRequest, RecommendByCountryRequest, RecommendByMenuTypeRequest

router = APIRouter()

@router.post("/flavor/")
async def recommend_by_flavor(db: SessionDep, obj_in: RecommendByFlavorRequest) -> None:
    recommendation_service = RecommendationService()
    result_data = await recommendation_service.recommend_by_flavor(db=db, obj_in=obj_in)
    return

@router.post("/ingredient/")
async def recommend_by_ingredient(db: SessionDep, obj_in: RecommendByIngredientRequest) -> None:
    recommendation_service = RecommendationService()
    result_data = await recommendation_service.recommend_by_ingredient(db=db, obj_in=obj_in)
    return

@router.get("/type/")
async def recommend_by_menu_type(db: SessionDep, obj_in: RecommendByMenuTypeRequest) -> None:
    recommendation_service = RecommendationService()
    result_data = await recommendation_service.recommend_by_menu_type(db=db, obj_in=obj_in)
    return

@router.get("/country/")
async def recommend_by_country(db: SessionDep, obj_in: RecommendByCountryRequest) -> None:
    recommendation_service = RecommendationService()
    result_data = await recommendation_service.recommend_by_country(db=db, obj_in=obj_in)
    return
