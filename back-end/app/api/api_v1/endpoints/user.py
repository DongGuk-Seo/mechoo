from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlmodel import select
from api.deps import SessionDep
from models.user import User

router = APIRouter()

@router.get("/", dependencies=[])
def read_user(session: SessionDep) -> Optional[User]:
    statement = select(User)
    user = session.exec(statement).first()
    return user