from bson import ObjectId

def serialize_item(item):
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "description": item.get("description", "")
    }
