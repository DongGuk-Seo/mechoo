from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Token(Base):
    __tablename__ = "token"
    
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    refresh_token: Mapped[str] = mapped_column(String, index=True)
    localtion: Mapped[str] = mapped_column(String, nullable=False, default=False)
    is_expired: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)