import pymongo
from django.conf import settings
import os
from bson.json_util import dumps



class MongoClient:

    def __init__(self, collection_name):
        self.client = 'mongodb+srv://'+os.environ['MONGO_USER']+':'+os.environ['MONGO_PASSWORD']+'@'+os.environ['MONGO_HOST']+'/?retryWrites=true&w=majority'
        db = os.environ['MONGO_DB']
        print("=======", self.client)
        self.db = self.client['stock_monitor']
        self.table = self.db[collection_name]

    def getAll(self):
        cursor = self.table.find()
        return dumps(cursor)


#         # Create two documents
# medicine_1 = {
#     "medicine_id": "RR000123456",
#     "common_name": "Paracetamol",
#     "scientific_name": "",
#     "available": "Y",
#     "category": "fever"
# }
# medicine_2 = {
#     "medicine_id": "RR000342522",
#     "common_name": "Metformin",
#     "scientific_name": "",
#     "available": "Y",
#     "category": "type 2 diabetes"
# }

# # Insert the documents
# collection_name.insert_many([medicine_1, medicine_2])

# # Check the count
# count = collection_name.count()
# print(count)

# # Read the documents
# med_details = collection_name.find({})

# # Print on the terminal
# for r in med_details:
#     print(r["common_name"])

# # Update one document
# update_data = collection_name.update_one({'medicine_id': 'RR000123456'}, {
#                                          '$set': {'common_name': 'Paracetamol 500'}})

# # Delete one document
# delete_data = collection_name.delete_one({'medicine_id': 'RR000123456'})
