"""

 TO MAKE A VIRTUAL PROJECT : - python -m venv .venv
 TO ACTIVATE THE VIRTUAL PROJECT : - source .venv/bin/activatepip install fastapi uvicorn
 TO INSTALL FASTAPI : - pip install fastapi uvicorn
 TO VERIFY FAST API IS INSTALLED OR NOT : - python -c "import fastapi; print(fastapi.__version__)"
-> install required package to connect with database : -pip install sqlalchemy psycopg2-binary asyncpg alembic
  note: - sqlalchemy: ORM for handling database operations.
        psycopg2-binary: PostgreSQL adapter for synchronous connections.
        asyncpg: High-performance PostgreSQL driver for async operations.
        alembic: Database migrations.

-> To load environment variables from a .env file: - pip install python-dotenv


"""