from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import response, schemas

from .controllers import StockController


@api_view(['GET'])
def stocks(request):
    stock = StockController()
    a = stock.getStores()
    print("============ ", a)
    return JsonResponse(a)


@api_view(['GET', 'POST', 'DELETE'])
def stock_details(request):
    # try:
    #     stock = Stock.objects.get(pk=pk)
    # except Stock.DoesNotExist:
    return JsonResponse({'message': 'The stock does not exist'}, status=status.HTTP_404_NOT_FOUND)
