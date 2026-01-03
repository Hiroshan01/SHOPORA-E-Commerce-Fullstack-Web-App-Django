from django.db import models

# Create your models here.
class Stock(models.Model):
    quantity = models.PositiveBigIntegerField(default=0)
    low_stock_threshold = models.PositiveBigIntegerField(default=0)
    product = models.OneToOneField('catalog.Product', on_delete=models.CASCADE)