from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session
from fastapi import HTTPException
from core.security import get_password_hash, verify_password
from crud.base import CRUDBase
from models.user import User
from schemas.user import UserCreate, UserUpdate

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_user_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()
    
    def get_user_by_username(self, db: Session, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()
    
    def valid_exist_user(self, db: Session, email: str, username: str) -> None:
        is_email_exist =  db.query(User).filter(User.email == email).first()
        is_username_exist =  db.query(User).filter(User.username == username).first()
        if is_email_exist:
            raise HTTPException(
            status_code=400,
            detail="이미 존재하는 이메일입니다."
        )
        if is_username_exist:
            raise HTTPException(
            status_code=400,
            detail="이미 존재하는 유저 이름입니다."
        )

    def create(self, db: Session, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            username=obj_in.username,
            password=get_password_hash(obj_in.password),
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, email: str, password: str) -> Optional[User]:
        user = self.get_user_by_email(db, email=email)
        if not user:
            raise HTTPException(204, "존재하지 않는 유저입니다.")
        if not verify_password(password, user.password):
            raise HTTPException(204, "틀린 비밀번호 입니다.")
        return user

user = CRUDUser(User)