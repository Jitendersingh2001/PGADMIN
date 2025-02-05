from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text  # Import the text function
from core.database import database

app = FastAPI()

@app.get("/example")
async def example_route(db: AsyncSession = Depends(database.get_db)):
    # Use the database session and wrap the query in text()
    result = await db.execute(text("SELECT 1"))
    return {"result": result.scalar()}
