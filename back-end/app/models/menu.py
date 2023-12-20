from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from models.base import Base

class Menu(Base):
    __tablename__ = "menu"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(String, index=True)
    summary: Mapped[str] = mapped_column(String)

class MenuDetail(Base):
    __tablename__ = "menu_detail"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    menu_id: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    sweet_level: Mapped[int] = mapped_column(Integer, nullable=False)
    hot_level: Mapped[int] = mapped_column(Integer, nullable=False)
    sour_level: Mapped[int] = mapped_column(Integer, nullable=False)
    oil_level: Mapped[int] = mapped_column(Integer, nullable=False)
    include_meet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    include_veget: Mapped[bool] = mapped_column(Boolean , nullable=False)
    food_type: Mapped[str] = mapped_column(String, nullable=False)
    country: Mapped[str] = mapped_column(String, nullable=False)

class MenuRecipe(Base):
    __tablename__ = "menu_recipe"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    menu_id: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    recipe: Mapped[str] = mapped_column(String)
    source_link: Mapped[str] = mapped_column(String)

class MenuImage(Base):
    __tablename__ = "menu_image"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    menu_id: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    image_url: Mapped[str] = mapped_column(String, nullable=False)

class Ingredient(Base):
    __tablename__ = "ingredient"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)

class MenuIngredient(Base):
    __tablename__ = "menu_ingredient"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    menu_id: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    ingredient_id: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
