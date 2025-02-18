from sqlalchemy.ext.asyncio import AsyncSession
from config.database import AsyncSessionLocal
from typing import AsyncGenerator

async def getDB() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency to provide a database session for route handlers.
    
    Ensures the session is properly closed after use, even if an exception occurs.
    This function is designed to be used as a FastAPI dependency.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception as e:
            # Rollback in case of an exception
            await session.rollback()
            raise
        finally:
            await session.close()