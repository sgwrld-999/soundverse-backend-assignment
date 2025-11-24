from app.database import SessionLocal, engine
from app import models

def seed_db():
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    if db.query(models.Clip).count() > 0:
        print("Database already seeded.")
        return

    clips = [
        models.Clip(
            title="Impact Intermezzo",
            description="A dramatic orchestral impact.",
            genre="Cinematic",
            duration=12.5,
            audio_url="https://cdn.pixabay.com/download/audio/2022/03/24/audio_1c1b809e87.mp3"
        ),
        models.Clip(
            title="Lofi Study",
            description="Chill lofi beats for studying.",
            genre="Lofi",
            duration=45.0,
            audio_url="https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3"
        ),
        models.Clip(
            title="Upbeat Pop",
            description="Energetic pop track.",
            genre="Pop",
            duration=30.0,
            audio_url="https://cdn.pixabay.com/download/audio/2022/10/25/audio_946859e751.mp3"
        ),
        models.Clip(
            title="Ambient Piano",
            description="Soothing piano melody.",
            genre="Ambient",
            duration=60.0,
            audio_url="https://cdn.pixabay.com/download/audio/2022/01/18/audio_d0a13f69d2.mp3"
        ),
         models.Clip(
            title="Electronic Groove",
            description="Synthesizer groove.",
            genre="Electronic",
            duration=25.0,
            audio_url="https://cdn.pixabay.com/download/audio/2022/03/15/audio_c8c8a73467.mp3"
        ),
    ]

    for clip in clips:
        db.add(clip)
    
    db.commit()
    print("Database seeded successfully!")
    db.close()

if __name__ == "__main__":
    seed_db()
