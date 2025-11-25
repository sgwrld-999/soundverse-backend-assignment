from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import schemas
from app.services.audio_service import audio_service

router = APIRouter()

@router.get("/", response_model=List[schemas.Clip])
def read_clips(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return audio_service.get_clips(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.Clip, status_code=status.HTTP_201_CREATED)
def create_clip(clip: schemas.ClipCreate, db: Session = Depends(get_db)):
    return audio_service.create_clip(db, clip)

@router.get("/{id}/stream")
def stream_clip(id: int, db: Session = Depends(get_db)):
    return audio_service.stream_clip(db, id)

@router.get("/{id}/stats", response_model=schemas.ClipStats)
def get_clip_stats(id: int, db: Session = Depends(get_db)):
    return audio_service.get_clip_stats(db, id)
