from tinydb import TinyDB
db = TinyDB('db.json')
db.truncate()
table_products = db.table('products')
table_specifications = db.table('specifications')
def insert_db(data_csv):
    data_csv = data_csv.read().split('\n')
    products = []
    column = data_csv[0].split(',')
    for row in data_csv[1:]:
        product = row.split(',')
        data = {}
        for i in range(len(column)):
            data[column[i]] = product[i]
        products.append(data)
    return products

products_db = insert_db(open('smartphone/products.csv'))
specifications_db = insert_db(open('smartphone/specifications.csv'))
table_products.insert_multiple(products_db)
table_specifications.insert_multiple(specifications_db)






