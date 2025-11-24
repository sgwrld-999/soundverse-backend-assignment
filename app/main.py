from fastapi import FastAPI
from starlette_exporter import PrometheusMiddleware, handle_metrics
from .database import engine, Base
from .routers import play

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Soundverse Play API")

# Add Prometheus middleware
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

app.include_router(play.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Soundverse Play API"}
