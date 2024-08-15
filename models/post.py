from pydantic import BaseModel
from datetime import datetime


class Post(BaseModel):
    title: str
    subtitle: str | None = None
    date: datetime = datetime.now()
    content: str