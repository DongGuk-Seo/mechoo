from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session
from fastapi import HTTPException
from core.security import get_password_hash, verify_password
from crud.base import CRUDBase
from models.token import Token
from schemas.token import TokenBase, TokenOutput, TokenInput, TokenUpdate

class CRUDToken(CRUDBase[Token, TokenBase, TokenOutput]):
    def get_user_by_refresh_token(self, db: Session, refresh_token: str) -> Token:
        token_model = db.query(Token).filter(Token.refresh_token == refresh_token).first()
        if token_model:
            return token_model
        raise HTTPException(204, "존재하지 않는 토큰입니다.")

    def create(self, db: Session, obj_in: TokenInput) -> Token:
        db_obj = Token(
            user_id=obj_in.user_id,
            refresh_token=obj_in.refresh_token,
            location=obj_in.location
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def expire_token(self, db: Session, db_obj: Token, obj_in: Union[TokenUpdate, Dict[str, Any]]) -> Token:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if not update_data["is_expired"]:
            del update_data["is_expired"]
            update_data["is_expired"] = True
        return super().update(db, db_obj=db_obj, obj_in=update_data)

token = CRUDToken(Token)