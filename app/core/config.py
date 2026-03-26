from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI PRD Generator"
    debug: bool = False

    llm_api_key: str = ""
    llm_provider: str = "ollama"
    llm_base_url: str = "https://unawares-needy-jettie.ngrok-free.dev/api/generate"
    model_name: str = "llama3"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()
