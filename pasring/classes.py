import typing
from Product import Product


class SubCatalog:
    __slots__ = ['name', 'url', 'product_list']

    def __init__(self, name, url, product_list: typing.List[Product]):
        self.name = name
        self.url = url
        self.product_list = product_list


class Catalog:
    __slots__ = ['name', 'sub_catalog_list']

    def __init__(self, name, sub_catalog_list: typing.List[SubCatalog]):
        self.name = name
        self.sub_catalog_list = sub_catalog_list
