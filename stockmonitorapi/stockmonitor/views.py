from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import response, schemas
from drf_yasg.utils import swagger_auto_schema
from .controllers import StockController

@api_view(['GET'])
def stocks(request):
    stock = StockController()
    result = stock.getStock()
    return JsonResponse(result, safe=False)

# @api_view(['DELETE'])
# def deleteStocks(request):
#     stock = StockController()
#     result = stock.deleteStock(request.id)
#     return JsonResponse(result, safe=False)

# @swagger_auto_schema(method='patch', auto_schema=None)
# @api_view(['PATCH'])
# def updateStocks(request):
#     stock = StockController()
#     result = stock.updateStock(request.id, request)
#     return JsonResponse(result, safe=False)
