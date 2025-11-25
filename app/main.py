from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette_exporter import PrometheusMiddleware, handle_metrics
from app.database import engine, Base
from app.api.v1.api import api_router
from app.core.config import settings

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

# Add Prometheus middleware
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)

# Mount static files for frontend
app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/health")
def health_check():
    return {"status": "ok"}
