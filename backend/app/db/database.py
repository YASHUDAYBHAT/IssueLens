from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(settings.MONGODB_URL)

db = client[settings.DATABASE_NAME]


async def ping_database():
    await client.admin.command("ping")