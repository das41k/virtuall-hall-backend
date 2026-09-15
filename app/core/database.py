from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from .config import settings

engine = create_async_engine(
    url = settings.DB_URL_asyncpg,
    echo = True,
    pool_size = 7,
    max_overflow = 10
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False
)

async def get_session():
    async with AsyncSessionLocal() as session:
        yield session
        
class Base(DeclarativeBase):
    pass