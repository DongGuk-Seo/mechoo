from app.core.config import settings

from sqlmodel import create_engine

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)