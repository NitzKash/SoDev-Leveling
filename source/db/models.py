from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from source.config import MONGO_URI, DB_NAME

# MongoDB Setup
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
quests_collection = db.quests
progress_collection = db.progress

# Quest model
class Quest(BaseModel):
    title: str
    description: str
    difficulty: str
    completed: bool = False