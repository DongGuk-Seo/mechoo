from fastapi import APIRouter
from api.api_v1.endpoints import user
from api.api_v1.endpoints import token

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(token.router, prefix="/token", tags=["token"])