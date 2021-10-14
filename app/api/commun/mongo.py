import os
from pymongo import MongoClient
from contextlib import contextmanager



@contextmanager
def collection(collection_name:str):
    
    with MongoClient(os.environ['MONGO_CONNECTION_STRING']) as conn: 
        col = conn[os.environ['MONGO_DATABASE_NAME']][collection_name]
        try:
            yield col
        finally:
            conn.close()
            
