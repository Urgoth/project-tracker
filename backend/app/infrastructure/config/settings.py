from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Project Tracker Backend"
    app_env: str = "dev"
    debug: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
    )


settings = Settings()
