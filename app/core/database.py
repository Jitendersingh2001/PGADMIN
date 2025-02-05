from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config.setting import settings

# Use the DATABASE_URL from settings
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Session Local setup
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Dependency to get the database session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
