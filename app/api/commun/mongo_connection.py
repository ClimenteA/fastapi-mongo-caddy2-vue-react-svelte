import os
import logging as log
from pymongo import MongoClient



def get_db():
    client = MongoClient(os.environ['MONGO_CONNECTION_STRING'])
    db = client.db
    return db