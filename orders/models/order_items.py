from django.db import models


class CartItem(models.Model):
    name_snapshot = models.CharField(max_length=120)
    price_snapshot = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE)
    product = models.ForeignKey("catalog.Product", on_delete=models.CASCADE)
