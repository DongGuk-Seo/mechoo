from typing import Optional

from fastapi import APIRouter, Request
from crud import token
from api.deps import SessionDep
from schemas.token import TokenBase, TokenInput, TokenOutput
from core.security import create_token

router = APIRouter()

@router.post("/reissue")
def reissue_token(session: SessionDep, token_in: TokenBase) -> Optional[TokenOutput]:
    token_model = token.get_user_by_refresh_token(session, token_in.refresh_token)
    if token_model:
        return