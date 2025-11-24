from pydantic import BaseModel
from typing import Optional

class ClipBase(BaseModel):
    title: str
    description: Optional[str] = None
    genre: str
    duration: float
    audio_url: str

class ClipCreate(ClipBase):
    pass

class Clip(ClipBase):
    id: int
    play_count: int

    class Config:
        orm_mode = True

class ClipStats(BaseModel):
    id: int
    title: str
    play_count: int
