from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from core.config import settings



DATABASE_URL = settings.SQLALCHEMY_DATABASE_URI
engine = create_async_engine(DATABASE_URL, echo=True)

# Create an async session factory
AsyncSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, class_=AsyncSession, expire_on_commit=False)
