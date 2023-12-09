from typing import Any, Optional
from datetime import timedelta

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlmodel import select

import crud
from api.deps import SessionDep
from core.security import create_token
from schemas.user import UserCreate, UserOutput, UserSignin

router = APIRouter()

@router.post("/signup")
def create_user(*, session: SessionDep, user_in: UserCreate) -> UserOutput:
    user = crud.user.valid_exist_user(db=session, email=user_in.email, username=user_in.username)
    user = crud.user.create(db=session, obj_in=user_in)
    res = UserOutput(
        id=user.id,
        email=user.email,
        username=user.username,
        )
    return res

@router.post("/signin")
def signin(*, session: SessionDep, user_in:UserSignin) -> Optional[str]:
    user = crud.user.authenticate(db=session, email=user_in.email, password=user_in.password)
    if user:
        access_token = create_token(user.email)
    else:
        return None