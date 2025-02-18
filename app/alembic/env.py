from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
from config.database import Base 
from config import envVariables
import models

# Use the centralized Base's metadata
target_metadata = Base.metadata
print("Tables detected by Alembic:", target_metadata.tables.keys())
# Interpret the config file for Python logging.
if context.config.config_file_name is not None:
    fileConfig(context.config.config_file_name)

# Override the sqlalchemy.url in the Alembic config with the one from settings
config = context.config
config.set_main_option("sqlalchemy.url", envVariables.DATABASE_URL)

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection):
    """Run migrations with the given connection."""
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    """Run migrations in 'online' mode."""
    # Create an asynchronous engine
    connectable = create_async_engine(envVariables.DATABASE_URL)

    # Run migrations asynchronously
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

if context.is_offline_mode():
    run_migrations_offline()
else:
    from asyncio import run  # Import asyncio.run for running async functions
    run(run_migrations_online())