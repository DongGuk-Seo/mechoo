from typing import Optional

from fastapi import APIRouter, Request
from crud import token
from api.deps import SessionDep
from schemas.token import TokenBase, TokenInput, TokenOutput
from core.security import create_token, valid_token

router = APIRouter()

@router.post("/reissue")
def reissue_token(request: Request,session: SessionDep, token_in: TokenBase) -> Optional[TokenOutput]:
    is_expired = valid_token(token_in.refresh_token)
    if not is_expired and request.client:
        token_model = token.expire_token(db=session, db_obj=token.get_user_by_refresh_token(session, token_in.refresh_token))
        tokens = create_token(token_model.user_id)
        obj_in = TokenInput(
            refresh_token=tokens.refresh_token, 
            user_id=token_model.user_id,
            location=request.client.host
            )
        token.create(db=session, obj_in=obj_in)
        res = TokenOutput(refresh_token=tokens.refresh_token, access_token=tokens.access_token)
        return res
    return None