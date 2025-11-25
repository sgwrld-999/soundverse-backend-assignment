from app.database import SessionLocal
from app import models

db = SessionLocal()
clips = db.query(models.Clip).all()
print(f"Found {len(clips)} clips:")
for clip in clips:
    print(f"ID: {clip.id}, Title: {clip.title}, URL: {clip.audio_url}")
db.close()
