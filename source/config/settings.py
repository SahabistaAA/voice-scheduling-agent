from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from loguru import logger

def find_env_file():
    """
    Locate a .env file by searching relative to this file's directory
    and parent directories.
    """
    current = Path(__file__).resolve().parent
    for _ in range(4):
        env_path = current / ".env"
        if env_path.exists():
            return str(env_path)
        current = current.parent
    return ".env"

ENV_FILE = find_env_file()

class VAPIConfig(BaseSettings):
    api_key: str
    phone_number_id: str = ""
    assistant_id: str = ""

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_prefix="VAPI_",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False
    )

class GoogleCalendarConfig(BaseSettings):
    credentials_file: str

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_prefix="GOOGLE_CALENDAR_",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False
    )

class GlobalConfig(BaseSettings):
    """
    Global configuration entry point with lazily
    initialized component configurations.
    """
    PROJECT_NAME: str = "Voice Scheduling Agent"
    VERSION: str = "1.0.0"
    PORT: int = 8000

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._vapi_config = None
        self._google_calendar_config = None

    @property
    def vapi_config(self) -> VAPIConfig:
        if self._vapi_config is None:
            self._vapi_config = VAPIConfig()
        return self._vapi_config

    @property
    def google_calendar_config(self) -> GoogleCalendarConfig:
        if self._google_calendar_config is None:
            self._google_calendar_config = GoogleCalendarConfig()
        return self._google_calendar_config

# Check if .env file exists and warn if not
if not Path(ENV_FILE).exists():
    logger.warning(f"\n.env file not found at: {ENV_FILE}")
    logger.warning("Please create a .env file with required configuration.")
    logger.warning("See .env.example for reference.\n")

settings = GlobalConfig()
