from typing import Annotated, Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session
from db.engine import engine

def get_db() -> Generator:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_db)]