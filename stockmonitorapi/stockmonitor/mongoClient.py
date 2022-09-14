from multiprocessing.dummy import Array
from pymongo import MongoClient
from django.conf import settings
import os
from bson import json_util



class MongoDbClient:

    def __init__(self, collection_name):
        self.client = MongoClient('mongodb+srv://'+os.environ['MONGO_USER']+':'+os.environ['MONGO_PASSWORD']+'@'+os.environ['MONGO_DOMAIN']+'/?retryWrites=true&w=majority')
        self.db = self.client[os.environ['MONGO_DB']]
        self.table = self.db[collection_name]

    def getAll(self):
        cursor = self.table.find()
        return json_util.dumps(cursor)

    def insertMany(self, items: Array):
        self.table.insert_many(items)

    def count(self): 
        self.table.count()

    def updateOne(self, key, updateItem):
        self.table.update_one(key, {'$set': updateItem})

    def deleteOne(self, key):
        self.table.delete_one(key)