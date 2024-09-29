from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.ext.asyncio.engine import AsyncEngine

from app.load_settings import read_settings

DATABASE_URL: str = read_settings("database_url", "database", "postgresql")

# SQLAlchemy 연결, 세션 클래스 생성
engine: AsyncEngine = create_async_engine(
    url=DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
)

AsyncSessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    class_=AsyncSession,
    expire_on_commit=False,
)


# DB 세션 생성 (제너레이터)
async def get_db():
    async with AsyncSessionLocal(bind=engine) as session:
        yield session
