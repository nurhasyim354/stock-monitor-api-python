from djongo import models

class Stock(models.Model): 
    productName = models.CharField(max_length=200, blank=False, default='')
    category = models.CharField(max_length=200, blank=False, default='')
    stock = models.IntegerField(blank=False, default= 0)
    createdAt = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return self.productName
        


