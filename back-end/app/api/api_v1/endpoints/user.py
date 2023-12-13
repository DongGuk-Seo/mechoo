from typing import Any, Optional

from fastapi import APIRouter, Request, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlmodel import select

import crud
from api.deps import SessionDep
from core.security import create_token
from schemas.user import UserCreate, UserOutput, UserSignin, UserBase, UsernameBase
from schemas.token import TokenOutput, TokenInput

router = APIRouter()

@router.post("/signup")
def create_user(session: SessionDep, user_in: UserCreate) -> UserOutput:
    user = crud.user.valid_exist_user(db=session, email=user_in.email, username=user_in.username)
    user = crud.user.create(db=session, obj_in=user_in)
    res = UserOutput(
        id=user.id,
        email=user.email,
        username=user.username,
        )
    return res

@router.post("/signin")
def signin(request: Request, session: SessionDep, user_in: UserSignin) -> Optional[TokenOutput]:
    user = crud.user.authenticate(db=session, email=user_in.email, password=user_in.password)
    if not request.client:
        raise HTTPException(400, "유효하지 않은 사용자입니다.")
    if user:
        tokens = create_token(user.id)
        obj_in = TokenInput(
            refresh_token=tokens.refresh_token, 
            user_id=user.id,
            location=request.client.host
            )
        crud.token.create(db=session, obj_in=obj_in)
        res = TokenOutput(refresh_token=tokens.refresh_token, access_token=tokens.access_token)
        return res
    else:
        return None

@router.post("/exist/email")
def check_exist_email(session: SessionDep, user_in: UserBase) -> bool:
    user = crud.user.get_user_by_email(db=session, email=user_in.email)
    return bool(user)

@router.post("/exist/username")
def check_exist_username(*, session: SessionDep, user_in: UsernameBase) -> bool:
    user = crud.user.get_user_by_username(db=session, username=user_in.username)
    return bool(user)
