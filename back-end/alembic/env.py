import os

def get_database():
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    server = os.getenv("POSTGRES_SERVER")
    database = os.getenv("POSTGRES_DB")
    return f'postgresql+psycopg://{user}:{password}@{server}/{database}'