from ..mongoClient import MongoClient

class StockController(MongoClient):

    def __init__(self):
        self.store = MongoClient('Store')
        self.stock = MongoClient('Stock')

    def getStores(self):
        return self.store.getAll()
