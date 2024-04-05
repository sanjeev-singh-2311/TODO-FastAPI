from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy_utils import database_exists, create_database
from .config import POSTGRES_URL

engine = create_engine(POSTGRES_URL)

if not database_exists(engine.url):
    create_database(engine.url)

SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

