from res_framework import serializers
from stockmonitor.models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = (
            'productName',
            'category',
            'stock'
        )
