from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:root@db:5432/desafio_fullstack"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)