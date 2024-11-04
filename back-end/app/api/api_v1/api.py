from fastapi import APIRouter
from api.api_v1.endpoints import user, token, menu, ingredient, recommendation

api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(token.router, prefix="/tokens", tags=["tokens"])
api_router.include_router(menu.router, prefix="/menus", tags=["menus"])
api_router.include_router(ingredient.router, prefix="/ingredients", tags=["ingredients"])
api_router.include_router(recommendation.router, prefix="/recommendations", tags=["recommendations"])