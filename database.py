from email.mime import base
from typing import Generator
from lib2to3.pytree import Base
from sqlalchemy.orm import declarative_base
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:haminhhan@localhost:5432/han_db", echo=True)

Base = declarative_base()

SessionLocal  = sessionmaker(bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()