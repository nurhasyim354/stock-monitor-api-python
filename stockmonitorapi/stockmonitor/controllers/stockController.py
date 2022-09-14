from multiprocessing.dummy import Array
from ..mongoClient import MongoDbClient


class StockController(MongoDbClient):

    def __init__(self):
        self.stock = MongoDbClient('Stock')
        self.store = MongoDbClient('Store')

    def getStock(self):
        return self.stock.getAll()

    def addStock(self, stock):
        return self.stock.insertMany(Array[stock])

    def deleteStock(self, stockId) :
        return self.stock.deleteOne({'id': stockId})

    def updateStock(self, stockId, updateItem):
        return self.stock.updateOne({'id': stockId}, updateItem)