import datetime

from db import Base
from sqlalchemy import Column, String, Integer, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__= "user"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(64), unique=True)
    email = Column(String(128), unique=True)
    password = Column(String(128))
    date = Column(DateTime)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)


class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(64))
    file = Column(String(128))
    description = Column(Text)
    date = Column(DateTime, default=datetime.datetime.now())
    user = Column(Integer, ForeignKey("user.id"))
    user_id = relationship("User")


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(64))
    video = Column(Integer, ForeignKey("videos.id"))
    videos_id = relationship("Video")
