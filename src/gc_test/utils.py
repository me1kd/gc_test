from peewee import *

data_source = [
    {'name': 'product_A', 'sku': 'A', 'price': 50.0, "trigger": 3, "tprice": 130.0},
    {'name': 'product_B', 'sku': 'B', 'price': 30.0, "trigger": 2, "tprice": 45.0}, 
    {'name': 'product_C', 'sku': 'C', 'price': 20.0, "trigger": 0, "tprice": 0.0},
    {'name': 'product_D', 'sku': 'D', 'price': 15.0, "trigger": 0, "tprice": 0.0},
]

def prods_str_to_dict(str_products):
    chars = [*str_products]
    return {x:chars.count(x) for x in chars}

database = SqliteDatabase('./products.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Product(BaseModel):
    name = TextField()
    price = FloatField()
    sku = TextField()
    tprice = FloatField()
    trigger = IntegerField()

    class Meta:
        table_name = 'product'

def get_models(lst_skus):
    products = Product.select().where(Product.sku << lst_skus)
    return products

def populate_models(data_source):
    for data_dict in data_source:
        Product.create(**data_dict)

def create_db(models):
    database.create_tables(models)