from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Приложение для библиотеки"
    description: str
    database_url: str

    class Config:
        env_file = '.env'

settings = Settings()