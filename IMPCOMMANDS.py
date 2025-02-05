"""

-> Activate the Virtual Environment: : - source env/bin/activate

-> install required package to connect with database : -pip install sqlalchemy psycopg2-binary asyncpg alembic
  note: - sqlalchemy: ORM for handling database operations.
        psycopg2-binary: PostgreSQL adapter for synchronous connections.
        asyncpg: High-performance PostgreSQL driver for async operations.
        alembic: Database migrations.

-> To load environment variables from a .env file: - pip install python-dotenv


"""