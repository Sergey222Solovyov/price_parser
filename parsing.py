from classes import Product
from get_html import get_html_data
from settings import PRODUCTS_LINK, \
    NEXT_PAGE_LINK, PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_URL, PAGE
from utils import complete_url_fullness


def parse_products(url):
    next_url = url + PAGE
    product_list = []
    products_exist = True
    while products_exist:
        products_exist = False
        html_data = get_html_data(url=next_url)
        for tag in (html_data('div', {'class': PRODUCTS_LINK})):
            name = tag.get(PRODUCT_NAME)
            price = tag.get(PRODUCT_PRICE)
            url = complete_url_fullness(tag.get(PRODUCT_URL))
            product_list.append(Product(name=name, price=price, url=url))
            products_exist = True
        try:
            next_url = complete_url_fullness(
                (html_data.find('a', {'class': NEXT_PAGE_LINK})).get('href'))
        except AttributeError:
            products_exist = False
    return product_list

