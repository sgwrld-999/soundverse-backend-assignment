from fastapi import APIRouter
from app.api.v1.endpoints import play

api_router = APIRouter()
api_router.include_router(play.router, prefix="/play", tags=["play"])
