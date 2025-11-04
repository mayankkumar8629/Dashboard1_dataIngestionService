import os
from psycopg_pool import AsyncConnectionPool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read DB URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Global pool variable (shared across the app)
db_pool: AsyncConnectionPool | None = None


async def init_db_pool():
    """
    Initialize the asynchronous PostgreSQL connection pool.
    Should be called once when FastAPI starts.
    """
    global db_pool
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL is not set in environment variables.")

    db_pool = AsyncConnectionPool(
        conninfo=DATABASE_URL,
        min_size=2,   # Minimum number of connections
        max_size=10,  # Maximum number of connections (tune based on load)
        open=False    # Open explicitly on startup
    )

    await db_pool.open()
    print("✅ Database connection pool initialized successfully.")


async def close_db_pool():
    """
    Close all connections in the pool gracefully.
    Called automatically on FastAPI shutdown.
    """
    global db_pool
    if db_pool:
        await db_pool.close()
        print("🛑 Database connection pool closed.")


async def get_connection():
    """
    Acquire a connection from the pool.
    Usage:
        async with get_connection() as conn:
            await conn.execute("SELECT * FROM table_name;")
    """
    if not db_pool:
        raise RuntimeError("Database pool is not initialized. Call init_db_pool() first.")

    async with db_pool.connection() as conn:
        yield conn
