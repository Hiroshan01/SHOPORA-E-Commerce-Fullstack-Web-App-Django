from django.db import models

# Create your models here.
class Payment(models.Model):
    Method_CHOICES = (
        ("card", "Card"),
        ("cash", "Cash"),
        
    )
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
        ("cancelled", "Cancelled"),
    )
    transaction_id = models.CharField(max_length=150, unique=True)
    method = models.CharField(max_length=5, choices=Method_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    paid_at = models.DateTimeField()
    order = models.OneToOneField("orders.Order", on_delete=models.CASCADE)
   