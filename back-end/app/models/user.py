from typing import Union

from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.engine import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(64), index=True)
    username = Column(String(64))
    password = Column(String)
    user_detail = relationship("UserDetail", back_populates="user")

class UserDetail(Base):
    __tablename__ = "user_detail"

    id = Column(Integer, primary_key=True, index=True)
    profile_image = Column(String, nullable=True)
    profile_intro = Column(String, nullable=True)
    phone_number = Column(String(13), nullable=True)
    gender = Column(Boolean, nullable=True)
    birth = Column(Date, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False, index=True)
    user = relationship("User", back_populates="user_detail")