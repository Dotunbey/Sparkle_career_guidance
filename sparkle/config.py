
import logging
# UPDATED IMPORT FOR PYDANTIC V2
from pydantic_settings import BaseSettings 
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = Field("Sparkle", validation_alias="APP_NAME")
    debug: bool = Field(False, validation_alias="DEBUG")
    log_level: str = Field("INFO", validation_alias="LOG_LEVEL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
logging.basicConfig(
    level=getattr(logging, settings.log_level.upper(), logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
