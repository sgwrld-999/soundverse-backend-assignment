#!/usr/bin/env python3
import requests
import json

# Your Cloud Run service URL
SERVICE_URL = "https://soundverse-api-85057359118.us-central1.run.app"

# Seed data
clips = [
    {
        "title": "Summer Vibes",
        "description": "Upbeat summer track by DJ Cool",
        "genre": "Electronic",
        "duration": 60.0,
        "audio_url": "https://www2.cs.uic.edu/~i101/SoundFiles/BabyElephantWalk60.wav"
    },
    {
        "title": "Night Drive",
        "description": "Smooth night vibes by The Waves",
        "genre": "Ambient",
        "duration": 60.0,
        "audio_url": "https://www2.cs.uic.edu/~i101/SoundFiles/CantinaBand60.wav"
    },
    {
        "title": "Morning Coffee",
        "description": "Relaxing morning beats by Chill Beats",
        "genre": "Lo-Fi",
        "duration": 60.0,
        "audio_url": "https://www2.cs.uic.edu/~i101/SoundFiles/ImperialMarch60.wav"
    }
]

# Add clips via API
for clip in clips:
    try:
        response = requests.post(f"{SERVICE_URL}/api/v1/play/", json=clip)
        if response.status_code == 201:
            print(f"✓ Added: {clip['title']}")
        else:
            print(f"✗ Failed to add {clip['title']}: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"✗ Error adding {clip['title']}: {e}")

# Verify
try:
    response = requests.get(f"{SERVICE_URL}/api/v1/play/")
    if response.status_code == 200:
        clips_list = response.json()
        print(f"\n✓ Successfully seeded! Total clips: {len(clips_list)}")
        for clip in clips_list:
            print(f"  - {clip['title']} ({clip['genre']})")
    else:
        print(f"\n✗ Failed to verify: {response.status_code}")
except Exception as e:
    print(f"\n✗ Error verifying: {e}")
