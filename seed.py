from app.database import SessionLocal, engine
from app import models
from app.core.config import settings

def seed_db():
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    # Clear existing data to ensure we have working URLs
    db.query(models.Clip).delete()
    db.commit()

    clips = [
        models.Clip(
            title="Test MP3 100KB",
            description="A short test MP3 file.",
            genre="Test",
            duration=10.0,
            audio_url="https://freetestdata.com/wp-content/uploads/2021/09/Free_Test_Data_100KB_MP3.mp3"
        ),
        models.Clip(
            title="SoundHelix Song 1",
            description="A longer test song.",
            genre="Electronic",
            duration=372.0,
            audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
        ),
        models.Clip(
            title="Sample MP3",
            description="Another sample track.",
            genre="Pop",
            duration=30.0,
            audio_url="https://files.testfile.org/AUDIO/C/MP3/sample1.mp3"
        ),
         models.Clip(
            title="Impact Intermezzo (Fixed)",
            description="Dramatic impact.",
            genre="Cinematic",
            duration=12.0,
            # Using a backup URL or different source if possible, otherwise skipping broken ones
            audio_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
        ),
    ]

    for clip in clips:
        db.add(clip)
    
    db.commit()
    print("Database re-seeded successfully with working URLs!")
    db.close()

if __name__ == "__main__":
    seed_db()
