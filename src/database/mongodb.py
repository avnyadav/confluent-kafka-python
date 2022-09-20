import pymongo
import os


import certifi
ca = certifi.where()

class MongodbOperation:

    def __init__(self) -> None:

        self.client = pymongo.MongoClient(f"mongodb+srv://iNeuron:{os.getenv('MONGO_DB_PASSWORD',None)}@ineuron-ai-projects.7eh1w4s.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)
        self.db_name="ineuron"


    def insert_many(self,collection_name,records:list):
        self.client[self.db_name][collection_name].insert_many(records)

    def insert(self,collection_name,record):
        self.client[self.db_name][collection_name].insert_one(record)

        
