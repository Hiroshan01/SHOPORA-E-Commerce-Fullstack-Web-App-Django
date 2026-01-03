from django.db import models


class ShippingAddress(models.Model):
    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    address = models.TextField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    order = models.OneToOneField("orders.Order", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
