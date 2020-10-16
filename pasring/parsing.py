import threading
from Product import Product
from file import add_product_to_file
from pasring.get_lists import get_catalog_list
from settings import PRODUCTS_LINK, \
    NEXT_PAGE_LINK, PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_URL, PAGE, first_catalog_part, second_catalog_part, \
    third_catalog_part, FILE
from utils import complete_url_fullness
from get_html import get_html_data


def parse_catalog(catalog_list):
    sub_catalog_parser_list = []
    for catalog in catalog_list:
        print(catalog)
        sub_catalog_parser = threading.Thread(target=parse_sub_catalog, name=catalog.name, args=(catalog,))
        sub_catalog_parser_list.append(sub_catalog_parser)
        sub_catalog_parser.start()
    for sub_catalog_parser in sub_catalog_parser_list:
        sub_catalog_parser.join()
    return catalog_list


def parse_sub_catalog(catalog):
    product_parser_list = []
    for sub_catalog in catalog.sub_catalog_list:
        product_parser = threading.Thread(target=parse_products, name=sub_catalog.name,
                                          args=(sub_catalog.url, sub_catalog.product_list, sub_catalog))
        product_parser_list.append(product_parser)
        product_parser.start()
    for product_parser in product_parser_list:
        product_parser.join()


def parse_products(url, product_list, sub_catalog):
    next_url = url + PAGE
    products_exist = True
    while products_exist:
        products_exist = False
        html_data = get_html_data(url=next_url)
        try:
            if len(html_data) < 3:
                products_exist = True
                print(sub_catalog.name)
                continue
        except TypeError:
            products_exist = True
            print(sub_catalog.name)
            continue
        for tag in (html_data('div', {'class': PRODUCTS_LINK})):
            name = tag.get(PRODUCT_NAME)
            price = tag.get(PRODUCT_PRICE)
            url = complete_url_fullness(url=tag.get(PRODUCT_URL))
            product = Product(name=name, price=price, url=url, is_available=True)
            product_list.append(Product(name=name, price=price, url=url, is_available=True))
            add_product_to_file(product, FILE)
            products_exist = True
        try:
            next_url = complete_url_fullness(
                (html_data.find('a', {'class': NEXT_PAGE_LINK})).get('href'))
        except AttributeError:
            products_exist = False


def parse_catalog_part(catalog_part, main_catalog_list):
    catalog_list = get_catalog_list(catalog_part)
    parse_catalog(catalog_list)
    for catalog in catalog_list:
        main_catalog_list.append(catalog)


def parse_all(catalog_list):
    parse_catalog_part(first_catalog_part, catalog_list)
    parse_catalog_part(second_catalog_part, catalog_list)
    parse_catalog_part(third_catalog_part, catalog_list)
