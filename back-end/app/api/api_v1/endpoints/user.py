from typing import Any, Optional

import crud
from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlmodel import select
from api.deps import SessionDep
from core.security import get_password_hash
from schemas.user import UserCreate, User, UserSignin

router = APIRouter()

@router.post("/create")
def create_user(*, session: SessionDep, user_in: UserCreate) -> User:
    user = crud.get_user_by_email(session=session, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="존재하는 유저 입니다."
        )
    user = crud.create_user(session=session, user_create=user_in)
    res = User(
        id=user.id,
        email=user.email,
        username=user.username,
        )
    return res

@router.post("/signin")
def signin(*, session: SessionDep, user_in:UserSignin) -> Any:
    user = crud.user.authenticate(db=session, email=user_in.email, password=user_in.password)
    if user:
        return user.email
    else:
        return "no"