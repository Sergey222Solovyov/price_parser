from get_html import get_html_data
from pasring.classes import Catalog, SubCatalog
from settings import PEREKRESTOK_URL, CATALOG_LINK, CATALOG_ID
from utils import complete_url_fullness


def get_catalog_list(catalog_part):
    catalog_list = []
    html_data = get_html_data(url=PEREKRESTOK_URL)
    for tag in (html_data('a', {'class': CATALOG_LINK})):
        catalog_name = tag.get_text()
        catalog_id = tag.get(CATALOG_ID)
        if catalog_name in catalog_part:
            sub_catalog_list = get_sub_catalog_list(html_data=html_data, catalog_id=catalog_id)
            catalog_list.append(Catalog(name=catalog_name, sub_catalog_list=sub_catalog_list))
    return catalog_list


def get_sub_catalog_list(html_data, catalog_id):
    sub_catalog_list = []
    for tag in (html_data('a', {'data-id': catalog_id})):
        name = tag.get_text()
        url = complete_url_fullness(tag.get('href'))
        sub_catalog_list.append(SubCatalog(name=name, url=url, product_list=[]))
    return sub_catalog_list


