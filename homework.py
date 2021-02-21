from tinydb import TinyDB, Query
db = TinyDB('db.json')
db.truncate()
table_products = db.table('products')
table_specifications = db.table('specifications')
productQuery = Query()

product_types = table_products.all()
products = {}

for i in product_types:
    products[ i['company'] ] = table_specifications.search(productQuery.company == i['company'])
    print(i['company'],len( products[ i['company'] ]))
print(products)






