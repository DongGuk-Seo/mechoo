from core.config import settings
from sqlmodel import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

settings.SQLALCHEMY_DATABASE_URI = settings.set_db_url()

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()
