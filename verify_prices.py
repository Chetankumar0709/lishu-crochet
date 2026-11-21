import sqlite3
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from django.test import Client
from products.models import Product

con = sqlite3.connect('db.sqlite3')
rows = con.execute('SELECT name, price FROM products_product ORDER BY name').fetchall()
con.close()
html = Client().get('/', HTTP_HOST='127.0.0.1').content.decode()
print('DB_ROWS=', rows)
print('MODEL_ROWS=', [(p.name, str(p.price)) for p in Product.objects.order_by('name')])
print('HTML_399=', '₹399' in html)
print('HTML_149=', '₹149' in html)
print('HTML_199=', '₹199' in html)
