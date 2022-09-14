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
