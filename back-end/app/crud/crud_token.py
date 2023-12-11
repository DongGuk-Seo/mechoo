from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session
from fastapi import HTTPException
from core.security import get_password_hash, verify_password
from crud.base import CRUDBase
from models.token import Token
from schemas.token import TokenBase, TokenOutput, AuthInput

class CRUDToken(CRUDBase[Token, TokenBase, TokenOutput]):
    def get_user_by_refresh_token(self, db: Session, *, refresh_token: str) -> Any:
        return db.query(Token).filter(Token.refresh_token == refresh_token).first()

    def create(self, db: Session, *, obj_in: AuthInput) -> None:
        db_obj = Token(
            user_id=obj_in.user_id,
            refresh_token=obj_in.refresh_token,
            location=obj_in.location
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return

    def update(self, db: Session, *, db_obj: Token, obj_in: str) -> None:
        return 

token = CRUDToken(Token)