from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra='ignore', env_file=(Path(__file__).parent / "../.env"))
    # Bot
    BOT_TOKEN: str

    # PostgreSQL:
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_SCHEME: str
    DB_ECHO_COMMAND: bool

    @property
    def dsn_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # LOG:
    LOG_LEVEL: str
    LOG_PATH: str
    LOG_NAME: str

settings = Settings()
