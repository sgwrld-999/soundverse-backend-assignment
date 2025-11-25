from fastapi.testclient import TestClient
from app.main import app
from app import models
from app.database import get_db, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest
from app.core.config import settings

# Use a separate test database or mock
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

API_V1_STR = settings.API_V1_STR

def test_read_clips():
    # Seed some data
    db = TestingSessionLocal()
    # Clear existing data
    db.query(models.Clip).delete()
    
    clip = models.Clip(title="Test Clip", genre="Test", duration=10.0, audio_url="http://example.com/audio.mp3")
    db.add(clip)
    db.commit()
    db.close()

    response = client.get(f"{API_V1_STR}/play/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["title"] == "Test Clip"

def test_stream_clip():
    response = client.get(f"{API_V1_STR}/play/")
    clip_id = response.json()[0]["id"]
    
    # Mock requests.get would be better, but for now we test 404 for non-existent
    response = client.get(f"{API_V1_STR}/play/9999/stream")
    assert response.status_code == 404

def test_get_stats():
    response = client.get(f"{API_V1_STR}/play/")
    clip_id = response.json()[0]["id"]
    
    response = client.get(f"{API_V1_STR}/play/{clip_id}/stats")
    assert response.status_code == 200
    assert "play_count" in response.json()

def test_frontend_serve():
    response = client.get("/")
    assert response.status_code == 200
    assert "Soundverse Play" in response.text
