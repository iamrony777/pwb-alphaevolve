"""Centralised runtime configuration using Pydantic BaseSettings.

Environment variables (defaults in brackets):

OPENAI_API_KEY    – Required for evolution step (no default)
OPENAI_MODEL      – Chat model name ["o3-mini"]
MAX_COMPLETION_TOKENS        – Token cap for LLM replies [4096]

SQLITE_DB         – Path to SQLite file ["~/.alphaevolve/programs.db"]
"""

from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import Field



class Settings(BaseSettings):
    # OpenAI
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    openai_model: str = Field("o3-mini", env="OPENAI_MODEL")
    max_completion_tokens: int = Field(4096, env="MAX_COMPLETION_TOKENS")

    # Storage
    sqlite_db: str = Field("~/.alphaevolve/programs.db", env="SQLITE_DB")



    class Config:
        env_file = ".env"


settings = Settings()
