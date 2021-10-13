import os
import logging as log
from pymongo import MongoClient
from contextlib import contextmanager



@contextmanager
def collection(collection_name:str):
    """ This assures we have maximum 2 connections open to mongo """
    conn = MongoClient(os.environ['MONGO_CONNECTION_STRING'])
    col = conn[os.environ['MONGO_DATABASE_NAME']][collection_name]
    try:
        yield col
    finally:
        conn.close()
        
