from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Clip(Base):
    __tablename__ = "clips"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    genre = Column(String, index=True)
    duration = Column(Float) # Duration in seconds
    audio_url = Column(String)
    play_count = Column(Integer, default=0)
