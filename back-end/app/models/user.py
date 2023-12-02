from typing import Union

from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.engine import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(64), index=True, nullable=False)
    username = Column(String(64), nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(Date, nullable=False, autoincrement=True)
    user_detail = relationship("UserDetail", back_populates="user")

class UserDetail(Base):
    __tablename__ = "user_detail"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    profile_image = Column(String, nullable=True)
    profile_intro = Column(String, nullable=True)
    phone_number = Column(String(13), nullable=True)
    gender = Column(Boolean, nullable=True)
    birth = Column(Date, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False, index=True)
    user = relationship("User", back_populates="user_detail")