# Soundverse Play API

Backend service for the "Play" feature, built with FastAPI, PostgreSQL, and Prometheus/Grafana monitoring.

## Features

- **List Clips:** `GET /play` — Returns a list of available sound clips.
- **Stream Clip:** `GET /play/{id}/stream` — Streams the audio file and increments play count.
- **Get Stats:** `GET /play/{id}/stats` — Returns play count and metadata.
- **Add Clip:** `POST /play` — Add a new clip (Bonus).
- **Monitoring:** Prometheus metrics exposed at `/metrics`.

## Tech Stack

- **Framework:** FastAPI (Python 3.9)
- **Database:** PostgreSQL (SQLAlchemy ORM)
- **Monitoring:** Prometheus + Grafana (via starlette_exporter)
- **Deployment:** Docker Compose (Local), Cloud Run (Production)
- **Frontend:** Static HTML/CSS/JS (served via FastAPI)

## Implementation Details

### Architecture

- **Modular Structure:** The codebase is organized using a clean architecture pattern:
  - `app/models.py`: SQLAlchemy models define the database schema.
  - `app/schemas.py`: Pydantic schemas for request/response validation.
  - `app/repositories/`: Data access layer, with generic and clip-specific repositories.
  - `app/services/`: Business logic, e.g., audio streaming and play count increment.
  - `app/api/v1/endpoints/`: API route handlers.
  - `app/core/config.py`: Centralized configuration using pydantic-settings.
  - `app/database.py`: Database engine and session management.
  - `static/`: Frontend assets (HTML, CSS, JS).

- **Coding Style:**
  - Follows PEP8 and type hints throughout.
  - Docstrings are used for models and schemas.
  - Dependency injection via FastAPI's `Depends`.
  - Separation of concerns: API, service, repository, and model layers.

### API Design

- **RESTful Endpoints:** All endpoints follow REST conventions.
- **Validation:** Pydantic models ensure strict validation of input/output.
- **Streaming:** Audio files are streamed using FastAPI's `StreamingResponse`.
- **Play Count:** Each stream increments the play count atomically in the database.

### Database

- **PostgreSQL:** Used for persistent storage of clip metadata and play counts.
- **Seeding:** `seed.py` and `seed_remote.py` scripts populate the database with sample clips using public MP3 URLs.

### Monitoring

- **Prometheus:** Integrated via `starlette_exporter` middleware for request/stream metrics.
- **Grafana:** Configured for dashboard visualization (local access via Docker Compose).

### Frontend

- **Static Files:** Served via FastAPI's `StaticFiles` mount.
- **Single Page:** Simple HTML/CSS/JS frontend lists clips and allows streaming.

### Testing

- **Unit Tests:** Located in `tests/`, using FastAPI's TestClient and pytest.
- **Test Database:** SQLite used for isolated test runs.

### Deployment

- **Dockerized:** Multi-stage Dockerfile for efficient builds.
- **Cloud Run:** Production deployment uses Google Cloud Run, with environment-based config.
- **Local Dev:** Docker Compose spins up DB, Prometheus, and Grafana for local development.

## Project Structure

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── api.py
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           └── play.py
│   ├── repositories/
│   │   ├── base.py
│   │   └── clip_repository.py
│   └── services/
│       ├── __init__.py
│       └── audio_service.py
├── docker-compose.yml
├── Dockerfile
├── prometheus.yml
├── requirements.txt
├── seed.py
├── seed_remote.py
├── check_db.py
├── test_script.py
├── verify_script.py
├── static/
│   ├── app.js
│   ├── index.html
│   └── style.css
├── docs/
│   ├── assignment.md
│   └── VIDEO_SCRIPT.md
├── tests/
│   └── test_api.py
└── submission_summary.json
```

## Coding Style & Best Practices

- **Type Safety:** All models and functions use type hints.
- **Layered Design:** Clear separation between API, business logic, and data access.
- **Config Management:** All environment variables and settings are managed via pydantic-settings.
- **Error Handling:** Consistent use of HTTPException for API errors.
- **Extensibility:** Easily add new endpoints or features due to modular design.

## How to Run

See the "Setup & Running" section above for local and production instructions.

