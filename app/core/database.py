from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from config.setting import settings
import logging

logger = logging.getLogger(__name__)

class Database:
    # Singleton instance
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Initialize the database engine and session factory."""
        if not settings.DATABASE_URL:
            raise ValueError("DATABASE_URL must be set in the configuration.")

        self.engine = create_async_engine(settings.DATABASE_URL, echo=False)
        self.AsyncSessionLocal = sessionmaker(
            bind=self.engine, class_=AsyncSession, expire_on_commit=False
        )
        logger.info("Database engine and session factory initialized.")

    async def get_db(self):
        """Dependency to get the database session."""
        async with self.AsyncSessionLocal() as session:
            try:
                yield session
            except Exception as e:
                logger.error(f"An error occurred while using the database session: {e}")
                raise

# Singleton instance of the Database class
database = Database()