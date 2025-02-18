from fastapi import FastAPI
from routes import mainRouter
from core.dependencies import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from sqlalchemy import text  # Import the text function

app = FastAPI()

# Include the main router
app.include_router(mainRouter)

# Testing route to verify database connectivity
@app.get("/test-db-connection")
async def test_db_connection(db: AsyncSession = Depends(get_db)):
    """
    Test endpoint to verify database connectivity.
    Executes a simple query to check if the database is reachable.
    """
    try:
        # Perform a simple query to check the connection
        result = await db.execute(text("SELECT 1"))  # Wrap the query with text()
        return {"message": "Database connection successful", "result": result.scalar()}
    except Exception as e:
        return {"message": "Database connection failed", "error": str(e)}