from fastapi import APIRouter
from api.api_v1.endpoints import user, token, menu, ingredient, recommendation

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(token.router, prefix="/token", tags=["token"])
api_router.include_router(menu.router, prefix="/menu", tags=["menu"])
api_router.include_router(ingredient.router, prefix="/ingredient", tags=["ingredient"])
api_router.include_router(recommendation.router, prefix="/recommendation", tags=["recommendation"])