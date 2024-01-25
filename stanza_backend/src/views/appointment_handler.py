from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client.stanza_copy

houses = db.houses


def schedule_appointment(data: dict):
    pg_name = data["pg_name"]
    data = houses.find_one({"place": pg_name}, {"_id": False})
    if data:
        return True 
    else:
        return False