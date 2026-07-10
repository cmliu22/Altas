from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    provider: str = "mock"

    model: str = "default"

    api_key: str | None = None

    base_url: str | None = None


    class Config:
        env_file = ".env"