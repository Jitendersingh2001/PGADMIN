from fastapi import FastAPI
from routes import mainRouter  # Single import for all routes

app = FastAPI()

app.include_router(mainRouter)
