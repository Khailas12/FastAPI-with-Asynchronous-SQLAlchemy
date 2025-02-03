from typing import AsyncGenerator
from db.session import AsyncSessionLocal


async def get_db() -> AsyncGenerator:
    async with AsyncSessionLocal() as db: 
        yield db 
    # No need for db.close() since async with handles it
