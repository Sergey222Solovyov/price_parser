from classes import Catalog, SubCatalog
from parsing import parse_products
from get_html import get_html_data
from settings import PEREKRESTOK_URL, CATALOG_LINK, needless_catalogs, CATALOG_ID
from utils import complete_url_fullness


def get_catalog_list():
    html_data = get_html_data(url=PEREKRESTOK_URL)
    catalog_list = []
    for tag in (html_data('a', {'class': CATALOG_LINK})):
        name = tag.get_text()
        if name in needless_catalogs:
            continue
        else:
            sub_catalog_list = get_sub_catalog_list(catalog_id=tag.get(CATALOG_ID), html_data=html_data)
            catalog_list.append(Catalog(name=name, sub_catalog_list=sub_catalog_list))
    return catalog_list


def get_sub_catalog_list(html_data, catalog_id):
    sub_catalog = []
    for tag in (html_data('a', {'data-id': catalog_id})):
        name = tag.get_text()
        url = complete_url_fullness(tag.get('href'))
        product_list = parse_products(url=url)
        sub_catalog.append(SubCatalog(name=name, url=url, product_list=product_list))
    return sub_catalog
