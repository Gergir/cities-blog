from pydantic import BaseModel
from datetime import datetime
from services.db_service import Base, engine
from sqlalchemy import Column, Integer, String, DateTime

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    subtitle = Column(String)
    date = Column(DateTime)
    content = Column(String)

Base.metadata.create_all(bind=engine)


class PostRequest(BaseModel):
    title: str
    subtitle: str | None = None
    date: datetime = datetime.now()
    content: str


class PostResponse(BaseModel):
    id: int
    title: str
    date: datetime
    content: str
