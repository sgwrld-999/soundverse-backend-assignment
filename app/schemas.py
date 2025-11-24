# standards imports
from typing import Optional

# third party imports
from pydantic import BaseModel, Field


class ClipBase(BaseModel):
    """
    ClipBase model
    """
    title: str = Field(..., description="The title of the audio clip")
    description: Optional[str] = Field(None, description="A brief description of the audio clip")
    genre: str = Field(..., description="The genre of the audio clip")
    duration: float = Field(..., description="The duration of the audio clip in seconds")
    audio_url: str = Field(..., description="The URL to the audio file")


class ClipCreate(ClipBase):
    """
    ClipCreate model
    """
    pass


class Clip(ClipBase):
    """
    Clip model
    """
    id: int = Field(..., description="The unique identifier of the clip")
    play_count: int = Field(..., description="The number of times the clip has been played")

    class Config:
        orm_mode = True


class ClipStats(BaseModel):
    """
    ClipStats model
    """
    id: int = Field(..., description="The unique identifier of the clip")
    title: str = Field(..., description="The title of the audio clip")
    play_count: int = Field(..., description="The number of times the clip has been played")

