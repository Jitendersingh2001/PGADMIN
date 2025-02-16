from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import envVariables

DATABASE_URL = envVariables.DATABASE_URL

# Create an asynchronous engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # Enables SQL query logging (disable in production)
)

# Create a session factory for async sessions
AsyncSessionLocal: sessionmaker[AsyncSession] = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Base class for models (SQLAlchemy 2.0+ best practice)
class Base(DeclarativeBase):
    pass
