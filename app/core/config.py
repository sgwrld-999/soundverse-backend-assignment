from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Soundverse Play API"
    DATABASE_URL: str = "postgresql://user:password@localhost/soundverse"
    API_V1_STR: str = "/api/v1"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
