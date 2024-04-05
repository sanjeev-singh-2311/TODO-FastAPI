from sqlalchemy import Column, Integer, String, Boolean
from .connections import Base, engine

class Todo(Base):
    __tablename__ = "Todo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    body = Column(String)
    status = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)
