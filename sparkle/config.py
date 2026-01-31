"""
Sparkle Backend Application - Configuration Module.

This module handles configuration management using Pydantic's BaseSettings.
It loads environment variables and provides a centralized configuration object.
"""

import logging
from pydantic import BaseSettings, Field

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """
    Application settings configuration.

    Attributes:
        app_name: The name of the application.
        debug_mode: Boolean flag to enable debug mode.
        ai_api_key: Mock API Key for external AI service (placeholder).
    """
    app_name: str = Field("Sparkle Career Guidance", env="APP_NAME")
    debug_mode: bool = Field(False, env="DEBUG_MODE")
    ai_api_key: str = Field("mock-api-key", env="AI_API_KEY") 
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instantiate settings
try:
    settings = Settings()
    logger.info(f"Loaded configuration for {settings.app_name}")
except Exception as e:
    logger.critical(f"Failed to load configuration: {e}")
    raise
