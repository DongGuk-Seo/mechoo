from typing import Union

from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from app.db.engine import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    username = Column(String)
    password = Column(String)

class UserDetail(Base):
    __tablename__ = "user_detail"

    user_id = ForeignKey(User)
    profile_image = Column(String)
    profile_intro = Column(String)
    phone_number = Column(String)
    gender = Column(Boolean)
    birth = Column(Date)