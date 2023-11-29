import os

from alembic import context
from sqlalchemy import engine_from_config
from logging.config import fileConfig

config = context.config

# fileConfig(config.config_file_name)

def get_database():
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    server = os.getenv("POSTGRES_SERVER")
    database = os.getenv("POSTGRES_DB")
    return f'postgresql+psycopg://{user}:{password}@{server}/{database}'