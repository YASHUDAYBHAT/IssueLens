from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "IssueLens"
    VERSION: str = "0.1.0"

    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "issuelens"

    GITHUB_API: str = "https://api.github.com"
    GITHUB_TOKEN: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()