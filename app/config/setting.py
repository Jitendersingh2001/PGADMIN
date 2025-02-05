import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    # Store DB credentials in a dictionary
    DB: dict = {
        "DB_HOST": os.getenv("DB_HOST", "localhost"),
        "DB_PORT": os.getenv("DB_PORT", "5432"),
        "DB_USER": os.getenv("DB_USER", "admin"),
        "DB_PASS": os.getenv("DB_PASS", "admin123"),
        "DATABASE_NAME": os.getenv("DATABASE_NAME", "pgrooms"),
    }

    # Construct DATABASE_URL for SQLAlchemy
    DATABASE_URL: str = (
        f"postgresql+asyncpg://{DB['DB_USER']}:{DB['DB_PASS']}@{DB['DB_HOST']}:{DB['DB_PORT']}/{DB['DATABASE_NAME']}"
    )

    # JWT Secret Key
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "default_secret")

# Create an instance of Settings
settings = Settings()
