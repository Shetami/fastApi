from datetime import datetime
from typing import List

from pydantic import BaseModel


class VideoBase(BaseModel):
    title: str
    description: str
    date: datetime = None
    file: str

    class Config:
        orm_mode = True


class VideoList(VideoBase):
    id: int


class User(BaseModel):
    id: int
    name: str


class VideoUpload(VideoBase):
    pass
