from fastapi import APIRouter

import api

routes = APIRouter()

routes.include_router(api.video_router, prefix="/api")
