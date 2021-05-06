import logging
from functools import lru_cache

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
)

from config import settings

logging.basicConfig(
    handlers=[logging.FileHandler("mq.log"), logging.StreamHandler()],
    format="%(asctime)s %(levelname)-8s: %(filename)s %(funcName)s %(lineno)s %(message)s",
    datefmt="%m-%d %H:%M:%S",
    level=logging.INFO,
)


@lru_cache()
def get_db() -> AsyncIOMotorDatabase:
    logging.info("Starting MongoDB connection.")
    client = AsyncIOMotorClient(settings.db_host, settings.db_port)
    db = client.get_database(settings.db_name)
    return db


@lru_cache()
def get_col(col_name: str) -> AsyncIOMotorCollection:
    return get_db().get_collection(col_name)
