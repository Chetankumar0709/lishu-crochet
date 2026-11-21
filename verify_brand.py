import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from django.test import Client
from products.models import SiteSettings

settings = SiteSettings.objects.first()
print('DB_BUSINESS=', repr(settings.business_name if settings else None))
print('DB_HERO=', repr(settings.hero_text if settings else None))

response = Client().get('/', HTTP_HOST='127.0.0.1')
html = response.content.decode('utf-8')
print('STATUS=', response.status_code)
print('NEW_BRAND=', 'Lishu Floral Creations' in html)
print('OLD_BRAND=', 'Lishu Crochet' in html)
print('NEW_HERO=', 'designed to preserve memories' in html)
print('OLD_HERO=', 'crochet gifts' in html)
