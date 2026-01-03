from django.db import models

#One Product has multiple images
class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    is_primary = models.BooleanField()
    product = models.ForeignKey('catalog.Product',on_delete=models.CASCADE)