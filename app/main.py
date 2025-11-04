from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.database import init_db_pool, close_db_pool, get_connection


# --- LIFESPAN HANDLER ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle startup and shutdown events for FastAPI"""
    # Startup
    await init_db_pool()
    print("✅ Database initialized at startup.")

    yield 

    # Shutdown
    await close_db_pool()
    print("🛑 Database connection closed on shutdown.")


# --- INITIALIZE FASTAPI APP ---
app = FastAPI(
    title="Data Ingestion Service",
    version="1.0.0",
    lifespan=lifespan
)


# --- SIMPLE HEALTH CHECK ROUTE ---
@app.get("/health")
async def health_check():
    """Simple health endpoint to verify the service and DB are running."""
    try:
        async for conn in get_connection():
            result = await conn.execute("SELECT 1;")
            value = result.fetchone()
        return {"status": "ok", "db": "connected" if value else "disconnected"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# --- ROOT ROUTE ---
@app.get("/")
def home():
    return {"message": "🚀 FastAPI Data Ingestion Service Running ✅"}


