from django.db import models

class Stock(models.Model): 
    productName = models.CharField(max_length=200, blank=False, default='')
    category = models.CharField(max_length=200, blank=False, default='')
    stock = models.CharField(max_length=200, blank=False, default='')