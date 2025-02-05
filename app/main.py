from fastapi import FastAPI
from config.setting import settings

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "FastAPI with PostgreSQL is working!",
        "db_host": settings.DB["DB_HOST"],  # Accessing DB_HOST from the DB dictionary
        "db_port": settings.DB["DB_PORT"],  # Accessing DB_PORT from the DB dictionary
        "jwt_secret": settings.JWT_SECRET_KEY[:5] + "..."  # Hide full key for security
    }
