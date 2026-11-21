import sqlite3

con = sqlite3.connect('db.sqlite3')
con.execute("UPDATE products_sitesettings SET business_name=?, copyright_text=?, hero_text=?", (
    'Lishu Floral Creations',
    '© {year} Lishu Floral Creations. All rights reserved.',
    'Thoughtfully handcrafted floral gifts, made with love and designed to preserve memories.',
))
con.executemany("UPDATE products_product SET price=? WHERE name=?", (
    ('399.00', 'Blush Rose Bouquet'),
    ('149.00', 'Pastel Bloom Pot'),
    ('199.00', 'Garden Crochet Basket'),
    ('199.00', 'Garden Floral Basket'),
))
con.commit()
print(con.execute("SELECT business_name, hero_text FROM products_sitesettings").fetchall())
print(con.execute("SELECT name, price FROM products_product ORDER BY name").fetchall())
con.close()
