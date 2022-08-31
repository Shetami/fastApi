import shutil
from typing import List
from fastapi import UploadFile, File, APIRouter, Form, Depends
from sqlalchemy.orm import Session

from models import Video
from utils import get_db
import db_service
from schemas import VideoUpload

video_router = APIRouter()


@video_router.post("/")
async def video_upload(title: str = Form(...), description: str = Form(...), video: UploadFile = File(...)):
    info = Video(title=title, description=description)
    with open(f'{video.filename}', 'wb') as buffer:
        shutil.copyfileobj(video.file, buffer)

    return {"ok"}


@video_router.post("/image", status_code=201)
async def image_upload(image: List[UploadFile] = File(...)):
    for img in image:
        with open(f'{img.filename}', 'wb') as buffer:
            shutil.copyfileobj(img.file, buffer)

    return {"ok"}


@video_router.get("/video")
async def get_video_list(db: Session = Depends(get_db)):
    videos = db_service.get_video_list(db)
    return videos


@video_router.get("/video/{video_pk}")
async def get_video(video_pk: int, db: Session = Depends(get_db)):
    return db_service.get_video(db=db, video_pk=video_pk)


@video_router.post("/video")
async def post_video(
        title: str = Form(...),
        description: str = Form(...),
        video: UploadFile = File(...),
        db: Session = Depends(get_db)):
    with open(f'{video.filename}', 'wb') as buffer:
        shutil.copyfileobj(video.file, buffer)
    item = VideoUpload(
        title=title,
        file=video.filename,
        description=description
    )
    videos = db_service.upload_video(db, item)
    return videos
