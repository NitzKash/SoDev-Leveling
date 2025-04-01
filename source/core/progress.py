from source.db.models import progress_collection
from source.config import LEVEL_THRESHOLD

class UserProgress:
    level_threshold: int = LEVEL_THRESHOLD

    async def add_xp(self, xp: int):
        progress = await progress_collection.find_one({})
        if not progress:
            progress = {"xp": 0, "level": 1}
            await progress_collection.insert_one(progress)

        new_xp = progress["xp"] + xp
        new_level = progress["level"]
        if new_xp >= self.level_threshold:
            new_level += 1
            new_xp = 0  # Reset XP for next level

        await progress_collection.update_one({}, {"$set": {"xp": new_xp, "level": new_level}})
        
    @staticmethod
    async def get_current_progress():
        progress_data = await progress_collection.find_one({})
        if not progress_data:
            progress_data = {"xp": 0, "level": 1}
            await progress_collection.insert_one(progress_data)
        return progress_data

# Create a singleton instance
progress = UserProgress()