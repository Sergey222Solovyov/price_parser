import typing


class Product:
    def __init__(self, name, price, url):
        pass


class Section:
    def __init__(self, name, url):
        self.name = name
        self.url = url


class SubCatalog:
    def __init__(self, name, url, section_list: typing.List[Section]):
        self.url = url
        self.name = name
        self.section_list = section_list


class Catalog:
    def __init__(self, name, sub_catalog_list: typing.List):
        self.name = name
        self.sub_catalog_list = sub_catalog_list
