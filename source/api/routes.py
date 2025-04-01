from fastapi import FastAPI, HTTPException
from typing import List

from source.db.models import Quest, quests_collection
from source.core.progress import progress

app = FastAPI()

@app.post("/quests/", response_model=Quest)
async def create_quest(quest: Quest):
    quest_dict = quest.dict()
    await quests_collection.insert_one(quest_dict)
    return quest

@app.get("/quests/", response_model=List[Quest])
async def get_quests():
    quests_cursor = quests_collection.find()
    quests = [Quest(**quest) async for quest in quests_cursor]
    return quests

@app.patch("/quests/{quest_id}")
async def complete_quest(quest_id: str):
    quest = await quests_collection.find_one({"_id": quest_id})
    if not quest:
        raise HTTPException(status_code=404, detail="Quest not found")
    await quests_collection.update_one({"_id": quest_id}, {"$set": {"completed": True}})
    xp_reward = 50  # Adjust XP rewards based on difficulty later
    await progress.add_xp(xp_reward)
    progress_data = await progress.get_current_progress()
    return {"message": "Quest completed", "current_xp": progress_data["xp"], "level": progress_data["level"]}

@app.get("/progress")
async def get_progress():
    progress_data = await progress.get_current_progress()
    return {"xp": progress_data["xp"], "level": progress_data["level"]}