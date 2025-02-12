from fastapi import FastAPI
from app.routes import userApi

app = FastAPI()

app.include_router(userApi.router)