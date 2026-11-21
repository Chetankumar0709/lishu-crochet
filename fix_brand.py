import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.execute(
    "UPDATE products_sitesettings SET business_name=?, copyright_text=?, hero_text=?",
    (
        'Lishu Floral Creations',
        '© {year} Lishu Floral Creations. All rights reserved.',
        'Thoughtfully handcrafted floral gifts, made with love and designed to preserve memories.',
    ),
)
con.commit()
print('updated_rows=', cur.rowcount)
print(con.execute('SELECT business_name, hero_text FROM products_sitesettings').fetchall())
con.close()
