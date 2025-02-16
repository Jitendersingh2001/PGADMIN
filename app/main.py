from fastapi import FastAPI
from routes import mainRouter
from config import Dependencies
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()
app.include_router(mainRouter)
@app.get("/items/")
async def get_items(db: AsyncSession = Dependencies.db):
    # Your logic here
    return {"message": "Success"}