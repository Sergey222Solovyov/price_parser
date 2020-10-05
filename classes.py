import typing


class Product:
    def __init__(self, name, price, url):
        self.name = name
        self.price = price
        self.url = url


class Section:
    def __init__(self, name, url, product_list: typing.List[Product]):
        self.name = name
        self.url = url
        self.product_list = product_list


class SubCatalog:
    def __init__(self, name, url, section_list: typing.List[Section]):
        self.name = name
        self.url = url
        self.section_list = section_list


class Catalog:
    def __init__(self, name, sub_catalog_list: typing.List[SubCatalog]):
        self.name = name
        self.sub_catalog_list = sub_catalog_list
