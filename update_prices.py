import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()

from products.models import Product

prices = {
    "Blush Rose Bouquet": "399",
    "Pastel Bloom Pot": "149",
    "Garden Crochet Basket": "199",
    "Garden Floral Basket": "199",
}

for product in Product.objects.all():
    if product.name in prices:
        product.price = prices[product.name]
        product.save(update_fields=["price", "updated_at"])
        print(product.name, product.price)
