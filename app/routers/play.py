from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import requests
from fastapi.responses import StreamingResponse
from .. import models, schemas, database

router = APIRouter(
    prefix="/play",
    tags=["play"],
)

@router.get("/", response_model=List[schemas.Clip])
def read_clips(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    clips = db.query(models.Clip).offset(skip).limit(limit).all()
    return clips

@router.post("/", response_model=schemas.Clip, status_code=status.HTTP_201_CREATED)
def create_clip(clip: schemas.ClipCreate, db: Session = Depends(database.get_db)):
    db_clip = models.Clip(**clip.dict())
    db.add(db_clip)
    db.commit()
    db.refresh(db_clip)
    return db_clip

@router.get("/{id}/stream")
def stream_clip(id: int, db: Session = Depends(database.get_db)):
    clip = db.query(models.Clip).filter(models.Clip.id == id).first()
    if not clip:
        raise HTTPException(status_code=404, detail="Clip not found")
    
    # Increment play count
    clip.play_count += 1
    db.commit()
    
    # Stream the audio file
    # For this assignment, we'll proxy the audio_url if it's external, 
    # or serve a dummy file if we had local files.
    # Since requirements say "simulate streaming by sending back the MP3 file",
    # and we are using external URLs, we can stream the content from the URL.
    
    def iterfile():
        with requests.get(clip.audio_url, stream=True) as r:
            r.raise_for_status()
            for chunk in r.iter_content(chunk_size=8192):
                yield chunk
                
    return StreamingResponse(iterfile(), media_type="audio/mpeg")

@router.get("/{id}/stats", response_model=schemas.ClipStats)
def get_clip_stats(id: int, db: Session = Depends(database.get_db)):
    clip = db.query(models.Clip).filter(models.Clip.id == id).first()
    if not clip:
        raise HTTPException(status_code=404, detail="Clip not found")
    return clip
