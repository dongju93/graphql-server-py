from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.orm import sessionmaker

from app.load_settings import read_settings

DATABASE_URL = read_settings("database_url", "database", "postgresql")

# SQLAlchemy 연결, 세션 클래스 생성
engine: AsyncEngine = create_async_engine(
    url=DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
)
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    class_=AsyncSession,
    expire_on_commit=False,
)


# DB 세션 생성 (제너레이터)
async def get_db():
    async with AsyncSessionLocal(bind=engine) as session:
        try:
            yield session
        finally:
            await session.close()
