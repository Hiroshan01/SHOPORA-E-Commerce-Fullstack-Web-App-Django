import random
from io import BytesIO

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from faker import Faker

from catalog.models import Category, Product, ProductImage

fake = Faker()


class Command(BaseCommand):
    help = "Seed catalog data with categories, products and images"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding catalog data....")

        # If you want to delete Old data
        # Product.objects.all().delete()
        # Category.objects.all().delete()

        categories = self.create_categories()
        products = self.create_products(categories)
        self.create_product_images(products)

        self.stdout.write(self.style.SUCCESS("Dummy data created successfully"))
        self.stdout.write(self.style.SUCCESS(f"Created {len(categories)} categories"))
        self.stdout.write(self.style.SUCCESS(f"Created {len(products)} products"))

    def create_categories(self):
        """Create Categories"""
        names = ("Electronics", "Accessories", "Mobile Devices")
        categories = []

        for name in names:
            cat, created = Category.objects.get_or_create(name=name)
            categories.append(cat)
            if created:
                self.stdout.write(f"Created category: {name}")
            else:
                self.stdout.write(f"Category already exists: {name}")

        return categories

    def create_products(self, categories):
        """Create Products"""
        products = []

        for _ in range(30):
            # Create Price
            price = random.randint(1500, 60000)
            compared_price = price + random.randint(500, 5000)

            product = Product.objects.create(
                name=f"{fake.unique.word().capitalize()} {fake.word().capitalize()}",
                description=fake.paragraph(nb_sentences=5),
                price=price,
                compared_price=compared_price,
                category=random.choice(categories),
                is_active=True,
            )
            products.append(product)
            self.stdout.write(f"Created product: {product.name}")

        return products

    def create_product_images(self, products):
        """Product images"""
        for product in products:
            # For one product images 2-4
            num_images = random.randint(2, 4)

            for i in range(num_images):
                # Placeholder image URL (640x480 size)
                image_url = f"https://picsum.photos/640/480?random={random.randint(1, 1000)}"

                try:
                    # Download Images
                    response = requests.get(image_url, timeout=10)
                    if response.status_code == 200:
                        image_file = ContentFile(response.content)

                        # First image primary
                        is_primary = i == 0

                        product_image = ProductImage.objects.create(
                            product=product, is_primary=is_primary
                        )

                        # Image save
                        product_image.image.save(
                            f"product_{product.id}_image_{i}.jpg", image_file, save=True
                        )

                        self.stdout.write(f"  Added image {i + 1} to {product.name}")

                except Exception as e:
                    self.stdout.write(self.style.WARNING(f"Could not download image: {str(e)}"))

        self.stdout.write(self.style.SUCCESS("Product images created successfully"))
