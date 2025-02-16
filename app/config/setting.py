from functools import lru_cache
from pydantic import BaseSettings, Field, SecretStr

class Settings(BaseSettings):
    # Database configuration
    DB_HOST: str = Field(..., env="DB_HOST")
    DB_PORT: str = Field(..., env="DB_PORT")
    DB_USER: str = Field(..., env="DB_USER")
    DB_PASS: SecretStr = Field(..., env="DB_PASS")
    DATABASE_NAME: str = Field(..., env="DATABASE_NAME")

    # JWT Secret Key
    JWT_SECRET_KEY: SecretStr = Field(..., env="JWT_SECRET_KEY")

    # Construct DATABASE_URL for SQLAlchemy
    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS.get_secret_value()}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DATABASE_NAME}"
        )
    class Config:
        env_file = ".env"

# Create a singleton instance of Settings
"""
LRU  It stands for Least Recently Used (LRU) Cache
"""
@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings() 