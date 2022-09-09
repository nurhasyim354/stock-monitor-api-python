from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import response, schemas


@api_view(['GET', 'POST', 'DELETE'])
def stocks(request):
    # to be implementd
    return JsonResponse({})

@api_view(['GET', 'POST', 'DELETE'])
def stock_details(request, pk):
    try:
        stock = Stock.objects.get(pk=pk)
    except Stock.DoesNotExist:
        return JsonResponse({'message': 'The stock does not exist'}, status=status.HTTP_404_NOT_FOUND)
