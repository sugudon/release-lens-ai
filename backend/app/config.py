from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ReleaseLens AI"
    app_description: str = "AI-powered software release risk and change-impact analysis"
    app_version: str = "0.1.0"
    app_env: str = "development"
    debug: bool = True

    openai_api_key: str

    langsmith_api_key: str
    langsmith_tracing: bool = True
    langsmith_project: str = "release-lens-ai"

    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "release_lens"
    postgres_user: str = "release_lens"
    postgres_password: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()