import pymongo
from config import MONGO_URI, BOT_USERNAME 

client = pymongo.MongoClient(MONGO_URI )
db = client[BOT_USERNAME]
database = db["users"]

#===================== User database ================================

async def is_served_user(user_id: int) -> bool:
    user =  database.find_one({"bot_users": user_id})
    if not user:
        return False
    return True

async def get_served_users() -> list:
    users = database.find({"bot_users": {"$gt": 0}})
    if not users:
        return []
    users_list = []
    for user in users:
        users_list.append(user)
    return users_list

async def add_served_user(user_id: int):
    is_served = await is_served_user(user_id)
    if is_served:
        return
    return database.insert_one({"bot_users": user_id})

async def remove_served_user(user_id: int):
    is_served = await is_served_user(user_id)
    if is_served:
        return
    return await database.delete_one({"bot_users": user_id})

#===================== groups  database ================================

async def get_served_chats() -> list:
    chats = database.find({"chat_id": {"$lt": 0}})
    if not chats:
        return []
    chats_list = []
    for chat in database.find({"chat_id": {"$lt": 0}}):
        chats_list.append(chat)
    return chats_list

async def is_served_chat(chat_id: int) -> bool:
    chat = await database.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True

async def add_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if is_served:
        return
    return await database.insert_one({"chat_id": chat_id})

async def remove_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if not is_served:
        return
    return await database.delete_one({"chat_id": chat_id})

