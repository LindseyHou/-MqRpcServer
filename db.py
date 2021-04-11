from functools import lru_cache

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from config import settings


@lru_cache()
def get_db() -> AsyncIOMotorDatabase:
    print("Starting MongoDB connection.")
    client = AsyncIOMotorClient(settings.db_host, settings.db_port)
    db = client.get_database(settings.db_name)
    return db
