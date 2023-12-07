from typing import Union
from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped ,relationship, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    email: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    username: Mapped[str] = mapped_column(String(64), nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now())
    user_detail: Mapped["UserDetail"] = relationship("UserDetail", back_populates="user", cascade="all, delete-orphan")

class UserDetail(Base):
    __tablename__ = "user_detail"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    profile_image: Mapped[str] = mapped_column(String, nullable=True)
    profile_intro: Mapped[str] = mapped_column(String, nullable=True)
    phone_number: Mapped[str] = mapped_column(String(13), nullable=True)
    gender: Mapped[bool] = mapped_column(Boolean, nullable=True)
    birth: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False, index=True)
    user: Mapped["User"] = relationship("User", back_populates="user_detail")