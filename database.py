from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.ctn_bot
users = db.users

def get_user(user_id):
    user = users.find_one({"_id": user_id})
    if not user:
        user = {"_id": user_id, "balance": 0, "last_click": None, "referrals": 0, "taps": 0}
        users.insert_one(user)
    return user

def update_user(user_id, update):
    users.update_one({"_id": user_id}, {"$set": update})
