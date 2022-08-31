from sqlalchemy.orm import Session

from models import Video
from schemas import VideoUpload


def get_video_list(db: Session):
    return db.query(Video).all()


def get_video(db: Session, video_pk):
    return db.query(Video).get(video_pk)


def upload_video(db: Session, item: VideoUpload):
    video = Video(**item.dict())
    db.add(video)
    db.commit()
    db.refresh(video)
    return video
