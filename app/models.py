from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Clip(Base):
    """
    SQLAlchemy model representing an audio clip.

    Attributes:
        id (int): Unique identifier for the clip.
        title (str): Title of the audio clip.
        description (str): Brief description of the audio clip.
        genre (str): Genre of the audio clip.
        duration (float): Duration of the audio clip in seconds.
        audio_url (str): URL to the audio file.
        play_count (int): Number of times the clip has been played.
    """
    __tablename__ = "clips"

    id = Column(Integer, primary_key=True, index=True, doc="Unique identifier for the clip")
    title = Column(String, index=True, nullable=False, doc="Title of the audio clip")
    description = Column(String, nullable=True, doc="Brief description of the audio clip")
    genre = Column(String, index=True, nullable=False, doc="Genre of the audio clip")
    duration = Column(Float, nullable=False, doc="Duration of the audio clip in seconds")
    audio_url = Column(String, nullable=False, doc="URL to the audio file")
    play_count = Column(Integer, default=0, nullable=False, doc="Number of times the clip has been played")

    def __repr__(self):
        return f"<Clip(id={self.id}, title='{self.title}', genre='{self.genre}')>"

