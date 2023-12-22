from typing import Optional

from fastapi import APIRouter, Request, HTTPException
from crud import token
from api.deps import SessionDep
from schemas.token import TokenBase, TokenInput, TokenOutput
from core.security import create_token, valid_token
from core.utils import exception_401_unauthorized

router = APIRouter()



@router.post("/reissue")
def reissue_token(request: Request,session: SessionDep, token_in: TokenBase) -> Optional[TokenOutput]:
    valid = valid_token(token_in.refresh_token)
    
    # TODO : IP 교차검증 추가
    if not valid and request.client:
        token_model = token.get_user_by_refresh_token(session, token_in.refresh_token)
        if token_model.is_expired:
            raise exception_401_unauthorized("파기된 토큰입니다.")
        
        token.expire_token(db=session, db_obj=token_model)
        new_tokens = create_token(token_model.user_id)
        
        obj_in = TokenInput(
            refresh_token=new_tokens.refresh_token, 
            user_id=token_model.user_id,
            location=request.client.host
            )
        
        token.create(db=session, obj_in=obj_in)
        return TokenOutput(refresh_token=new_tokens.refresh_token, access_token=new_tokens.access_token)
    
    raise exception_401_unauthorized("토큰 검증에 실패하였습니다.")