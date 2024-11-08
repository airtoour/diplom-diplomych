from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TOKEN: str

    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    CARS_URL: str

    class Config:
        env_file = "D:/my-project/diplom-diplomych/.env"


settings = Settings()
