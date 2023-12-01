from typing import Union

from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.engine import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(64), index=True)
    username = Column(String(64))
    password = Column(String)

class UserDetail(Base):
    __tablename__ = "user_detail"

    profile_image = Column(String, nullable=True)
    profile_intro = Column(String, nullable=True)
    phone_number = Column(String(13), nullable=True)
    gender = Column(Boolean, nullable=True)
    birth = Column(Date, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)