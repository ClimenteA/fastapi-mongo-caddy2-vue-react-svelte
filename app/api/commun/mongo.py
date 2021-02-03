from pymongo import MongoClient
from urllib.parse import quote_plus


user = 'admin'
password = 'admin'
host = 'localhost'  #'mongo' #timeout

# uri = f"mongodb://{user}:{password}@{host}/?authSource=test_database&authMechanism=SCRAM-SHA-256"
# uri = "mongodb://%s:%s@%s" % (quote_plus(user), quote_plus(password), host)
# client = MongoClient(uri)

client = MongoClient(
    host, 
    username=user, 
    password=password, 
    authSource='the_database'
)




db = client.test_database
db = client['test-database']
collection = db.test_collection
collection = db['test-collection']

post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"]
}

posts = db.posts

post_id = posts.insert_one(post).inserted_id

print("Post added with ID:", post_id)

tables = db.list_collection_names()

print(tables)
