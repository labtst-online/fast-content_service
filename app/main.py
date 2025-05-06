import logging
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from importlib.metadata import version, PackageNotFoundError
from app.api.endpoints import router as post_router
from app.models.post import Post

from .core.config import settings
from .core.database import async_engine, get_async_session

# Configure logging
# Basic config, customize as needed (e.g., structured logging)
logging.basicConfig(level=logging.INFO if settings.APP_ENV == "production" else logging.DEBUG)
logger = logging.getLogger(__name__)

try:
    __version__ = version("fastboosty-profile_service")
except PackageNotFoundError:
    __version__ = "0.0.0"

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup...")
    # You can add startup logic here, like checking DB connection
    try:
        async with async_engine.connect():
            logger.info("Database connection successful during startup.")
    except Exception as e:
        logger.error(f"Database connection failed during startup: {e}")

    yield

    logger.info("Application shutdown...")
    # Close the engine connections pool
    await async_engine.dispose()
    logger.info("Database engine disposed.")


app = FastAPI(
    title="Content Service",
    description="Handles user contents.",
    version=__version__,
    lifespan=lifespan,
)

app.include_router(post_router, prefix="/content", tags=["Post"])


@app.get("/test-db/", summary="Test Database Connection", tags=["Test"])
async def test_db_connection(session: AsyncSession = Depends(get_async_session)):
    """
    Attempts to retrieve the first post_id from the database.
    """
    logger.info("Accessing /test-db/ endpoint")
    try:
        statement = select(Post).limit(1)
        result = await session.execute(statement)
        post = result.scalar_one_or_none()

        if post:
            logger.info(f"Successfully retrieved post_id: {post.id}")
            return {"status": "success", "first_post_id": post.id}
        else:
            logger.info("Noposts found in the database.")
            return {"status": "success", "message": "No posts found"}
    except Exception as e:
        logger.error(f"Database query failed: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Database error: {e}")


@app.get("/", summary="Health Check", tags=["Health"])
async def health_check():
    """Basic health check endpoint."""
    return {"status": "ok", "service": "Profile Service"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8002,  # Or load from config
        reload=(settings.APP_ENV == "development"),
        log_level="info",
    )
