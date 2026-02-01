"""
Sparkle Backend Application - Configuration Module.

This module handles configuration management using Pydantic's BaseSettings.
It loads environment variables and provides a centralized configuration object.
"""

#!filepath config.py
import logging
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    app_name: str = Field("Sparkle", env="APP_NAME")
    debug: bool = Field(False, env="DEBUG")
    log_level: str = Field("INFO", env="LOG_LEVEL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
logging.basicConfig(
    level=getattr(logging, settings.log_level.upper(), logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
