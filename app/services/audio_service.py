from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi.responses import StreamingResponse
import requests
from app.repositories.clip_repository import clip_repository
from app.schemas import ClipCreate, Clip as ClipSchema

class AudioService:
    def get_clips(self, db: Session, skip: int = 0, limit: int = 100):
        return clip_repository.get_multi(db, skip=skip, limit=limit)

    def create_clip(self, db: Session, clip_in: ClipCreate) -> ClipSchema:
        return clip_repository.create(db, clip_in.dict())

    def get_clip_stats(self, db: Session, clip_id: int):
        clip = clip_repository.get(db, clip_id)
        if not clip:
            raise HTTPException(status_code=404, detail="Clip not found")
        return clip

    def stream_clip(self, db: Session, clip_id: int):
        clip = clip_repository.get(db, clip_id)
        if not clip:
            raise HTTPException(status_code=404, detail="Clip not found")
        
        # Increment play count
        clip_repository.increment_play_count(db, clip)
        
        def iterfile():
            with requests.get(clip.audio_url, stream=True) as r:
                r.raise_for_status()
                for chunk in r.iter_content(chunk_size=8192):
                    yield chunk
                    
        return StreamingResponse(iterfile(), media_type="audio/mpeg")

audio_service = AudioService()
