from django.db import models

# class AuditModel(models.Model):
#     created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
#     create_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True


class Product(models.Model):
    # 1 - Idetity / Primary Key (id,uuid,ulid)
    # 2 - core bussiness attributes
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    sku = models.CharField(max_length=100)
    # 3 - slug /Humen readable identifier
    slug = models.SlugField(max_length=255, unique=True)
    # 4 - Status /flags /Enums
    is_active = models.BooleanField(default=True)
    # 5 - Pricing and inventory
    price = models.DecimalField(max_digits=10, decimal_places=2)
    compared_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    # 5 - Relations
    category = models.ForeignKey("catalog.Category", models.SET_NULL, null=True)
    # 6 - Timestamps(audit fields)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
