from django.db import models

from catalog.models import Product


class CartItem(models.Model):
    price_snapshot = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    cart = models.ForeignKey("cart.Cart", on_delete=models.CASCADE)
    product = models.ForeignKey(
        "catalog.Product", on_delete=models.CASCADE, related_name="cart_items"
    )
