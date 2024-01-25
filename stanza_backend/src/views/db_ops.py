import pymongo 
import re


client = pymongo.MongoClient("mongodb://localhost:27017")

db = client['stanza_copy']

houses = db.houses

def show_pg_search_res(pattern: str) -> list:
    pattern = pattern.lower()
    regex = re.compile(pattern, re.IGNORECASE)  # Use re.IGNORECASE for case-insensitive search
    query = {
        '$or': [
            {"locality": {'$regex': regex}},
            {"city": {'$regex': regex}}
        ]   
    }
    results = houses.find(query, {"locality":1, "city": 1})
    return list(results)

# data = show_pg_search_res('kat')
# print(data)