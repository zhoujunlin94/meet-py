import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    API_KEY: str
    DEBUG: bool = False

    class Config:
        env_file = os.getenv("ENV_FILE", ".env.test")  # 默认的env文件
        env_file_encoding = 'utf-8'

settings = Settings()