import uuid
from django.db import models
from django.utils.text import slugify


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
    sku = models.CharField(max_length=100, blank=True)
    # 3 - slug /Humen readable identifier
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    # 4 - Status /flags /Enums
    is_active = models.BooleanField(default=True)
    # 5 - Pricing and inventory
    price = models.DecimalField(max_digits=10, decimal_places=2)
    compared_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # 5 - Relations
    category = models.ForeignKey("catalog.Category", models.SET_NULL, null=True)
    # 6 - Timestamps(audit fields)
    create_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = f'{uuid.uuid4()}'[:30]
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1

            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1

            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug
