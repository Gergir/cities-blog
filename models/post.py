from optparse import Option
from typing import Optional

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
    creator = Column(String)
    image_url = Optional[Column(String)]
    content = Column(String)


class PostRequest(BaseModel):
    title: str
    subtitle: str | None = None
    date: datetime = datetime.now()
    creator: str = "Anonim"
    image_url: str | None = None
    content: str


class PostResponse(BaseModel):
    id: int
    title: str
    date: datetime
    content: str
