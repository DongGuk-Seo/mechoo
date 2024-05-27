from sqlalchemy import Boolean, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from models.base import Base

class Menu(Base):
    __tablename__ = "menu"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    summary: Mapped[str] = mapped_column(Text, default="", nullable=False)

class MenuDetail(Base):
    __tablename__ = "menu_detail"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    menu_id: Mapped[int] = mapped_column(Integer, nullable=False)
    sweet_level: Mapped[int] = mapped_column(Integer, nullable=False)
    sour_level: Mapped[int] = mapped_column(Integer, nullable=False)
    oil_level: Mapped[int] = mapped_column(Integer, nullable=False)
    spicy_level: Mapped[int] = mapped_column(Integer, nullable=False)
    is_cold_food: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    include_meat: Mapped[bool] = mapped_column(Boolean, nullable=False)
    include_veget: Mapped[bool] = mapped_column(Boolean , nullable=False)
    food_type_id: Mapped[int] = mapped_column(Integer, nullable=False)
    country_id: Mapped[int] = mapped_column(Integer, nullable=False)

class MenuRecipe(Base):
    __tablename__ = "menu_recipe"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    menu_id: Mapped[int] = mapped_column(Integer,  nullable=False)
    recipe: Mapped[str] = mapped_column(Text, default="", nullable=False)
    source_link: Mapped[str] = mapped_column(String(200))

class MenuImage(Base):
    __tablename__ = "menu_image"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    menu_id: Mapped[int] = mapped_column(Integer,  nullable=False)
    image_url: Mapped[str] = mapped_column(String, nullable=False)

class MenuIngredient(Base):
    __tablename__ = "menu_ingredient"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    menu_id: Mapped[int] = mapped_column(Integer,  nullable=False)
    ingredient_id: Mapped[int] = mapped_column(Integer,  nullable=False)

class FoodType(Base):
    __tablename__ = "food_type"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    type: Mapped[str] = mapped_column(String,  nullable=False)

class Country(Base):
    __tablename__ = "country"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(String,  nullable=False)