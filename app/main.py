from fastapi import FastAPI
from routes import mainRouter

app = FastAPI()
app.include_router(mainRouter)
