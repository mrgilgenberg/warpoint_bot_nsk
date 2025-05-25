from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from app.config import settings


engine_db = create_async_engine(url=settings.dsn_asyncpg, echo=settings.DB_ECHO_COMMAND)
sessions_db = async_sessionmaker(engine_db, expire_on_commit=False)
