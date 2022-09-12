from djongo import models

class Store(models.Model):
    name = models.CharField(max_length=200, default='')
    location=models.CharField(max_length=100, default='')
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productName


