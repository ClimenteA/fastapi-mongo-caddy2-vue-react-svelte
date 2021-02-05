from pymongo import MongoClient
from urllib.parse import quote_plus



uri = "mongodb://localhost:27017"
client = MongoClient(uri)

db = client.test_database
db = client['test-database']
collection = db.test_collection
collection = db['test-collection']

post = {
    "author": "Don John",
    "text": "First post on this container",
    "tags": ["mongodb", "python", "pymongo"]
}

posts = db.posts

post_id = posts.insert_one(post).inserted_id

print("Post added with ID:", post_id)

tables = db.list_collection_names()

print(tables)
