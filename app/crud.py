from bson import ObjectId
from app.database import collection
from app.models import serialize_item

def create_item(data: dict):
    result = collection.insert_one(data)
    return str(result.inserted_id)

def get_item(item_id: str):
    item = collection.find_one({"_id": ObjectId(item_id)})
    return serialize_item(item) if item else None

def get_all_items():
    return [serialize_item(item) for item in collection.find()]

def update_item(item_id: str, data: dict):
    collection.update_one({"_id": ObjectId(item_id)}, {"$set": data})
    return get_item(item_id)

def delete_item(item_id: str):
    result = collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count > 0
