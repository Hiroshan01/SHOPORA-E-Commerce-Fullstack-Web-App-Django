from django.db import models

class Order(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("PROCESSING", "Processing"),
        ("SHIPPED", "Shipped"),
        ("DELIVERED", "Delivered"),
        ("CANCELLED", "Cancelled"),
    )
    order_number = models.PositiveBigIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    sub_total = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    shipping_cost = models.PositiveIntegerField()
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
