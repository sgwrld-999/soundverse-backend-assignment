from sqlalchemy.orm import Session
from app.models import Clip
from app.repositories.base import BaseRepository

class ClipRepository(BaseRepository[Clip]):
    def increment_play_count(self, db: Session, clip: Clip) -> Clip:
        clip.play_count += 1
        db.add(clip)
        db.commit()
        db.refresh(clip)
        return clip

clip_repository = ClipRepository(Clip)
