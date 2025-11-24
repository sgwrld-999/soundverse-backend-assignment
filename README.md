# Soundverse Play API

Backend service for the "Play" feature, built with FastAPI, PostgreSQL, and Prometheus/Grafana monitoring.

## Features

- **List Clips**: `GET /play` - Returns a list of available sound clips.
- **Stream Clip**: `GET /play/{id}/stream` - Streams the audio file and increments play count.
- **Get Stats**: `GET /play/{id}/stats` - Returns play count and metadata.
- **Add Clip**: `POST /play` - Add a new clip (Bonus).
- **Monitoring**: Prometheus metrics exposed at `/metrics`.

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL (SQLAlchemy ORM)
- **Monitoring**: Prometheus + Grafana
- **Deployment**: Docker Compose (Local), Render/Railway (Production)

## Setup & Running

### Prerequisites

- Docker & Docker Compose
- Python 3.9+

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd sound0-verse-ai-assignment
   ```

2. **Start Services (DB, Prometheus, Grafana)**
   ```bash
   docker-compose up -d
   ```

3. **Install Dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Seed Database**
   ```bash
   python seed.py
   ```

5. **Run Application**
   ```bash
   uvicorn app.main:app --reload
   ```

   API will be available at `http://localhost:8000`.
   Docs at `http://localhost:8000/docs`.

### Monitoring

- **Grafana**: `http://localhost:3000` (admin/admin)
- **Prometheus**: `http://localhost:9090`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/play` | List all clips |
| POST | `/play` | Create a new clip |
| GET | `/play/{id}/stream` | Stream audio & increment count |
| GET | `/play/{id}/stats` | Get clip stats |
| GET | `/metrics` | Prometheus metrics |

## Project Structure

```
.
├── app
│   ├── main.py          # App entry point
│   ├── models.py        # Database models
│   ├── schemas.py       # Pydantic schemas
│   ├── database.py      # DB connection
│   └── routers
│       └── play.py      # Play API routes
├── docker-compose.yml   # Docker services
├── prometheus.yml       # Prometheus config
├── requirements.txt     # Python dependencies
└── seed.py             # Database seeder
```
