from pymongo import MongoClient
from bson.objectid import ObjectId
from app.config import Config
from app.services import generate_uuid, hash_password

from bson.errors import InvalidId

class UserModel:
    def __init__(self):
        self.client = MongoClient(Config.MONGO_URI)
        self.db = self.client["user_management"]
        self.collection = self.db["users"]

    def create_user(self, user_data):
        user_data["id"] = generate_uuid()
        user_data["password"] = hash_password(user_data["password"])
        return self.collection.insert_one(user_data).inserted_id

    def get_user(self, user_id):
        try:
            return self.collection.find_one({"id": user_id})
        except InvalidId:
            return None

    def get_all_users(self):
        return list(self.collection.find())

    def update_user(self, user_id, updated_data):
        # Hash password if present
        if "password" in updated_data:
            updated_data["password"] = hash_password(updated_data["password"])
        return self.collection.update_one(
            {"id": user_id}, 
            {"$set": updated_data}
        )

    def delete_user(self, user_id):
        return self.collection.delete_one({"id": user_id})