from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from models.base import Base

class Token(Base):
    __tablename__ = "token"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    refresh_token: Mapped[str] = mapped_column(String, index=True)
    location: Mapped[str] = mapped_column(String, nullable=False)
    is_expired: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)