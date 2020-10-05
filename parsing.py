import requests
from bs4 import BeautifulSoup
from classes import Catalog, SubCatalog, Section, Product
from settings import needless_catalogs,  PEREKRESTOK_URL, CATALOG_LINK, SECTIONS_LINK, PRODUCTS_LINK, \
    NEXT_PAGE_LINK, PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_URL, CATALOG_ID, PAGE
from utils import complete_url_fullness


def parse_catalog():
    html_data = get_html_data(url=PEREKRESTOK_URL)
    catalog_list = []
    for tag in (html_data('a', {'class': CATALOG_LINK})):
        name = tag.get_text()
        if name in needless_catalogs:
            continue
        else:
            sub_catalog_list = parse_sub_catalog(catalog_id=tag.get(CATALOG_ID), html_data=html_data)
            catalog_list.append(Catalog(name=name, sub_catalog_list=sub_catalog_list))
    return catalog_list


def parse_sub_catalog(html_data, catalog_id):
    sub_catalog = []
    for tag in (html_data('a', {'data-id': catalog_id})):
        name = tag.get_text()
        url = complete_url_fullness(tag.get('href'))
        sections_exist = check_sections_existence(url=url)
        if sections_exist:
            section_list = parse_section(url=url)
        else:
            product_list = parse_product(url=url)
            section_list = [Section(name=name, url=url, product_list=product_list)]
        sub_catalog.append(SubCatalog(name=name, url=url, section_list=section_list))
    return sub_catalog


def parse_section(url):
    section_list = []
    html_data = get_html_data(url=url)
    for tag in (html_data('a', {'class': SECTIONS_LINK})):
        name = tag.get_text(strip=True)
        url = complete_url_fullness(tag.get('href'))
        product_list = parse_product(url=url)
        section_list.append(Section(name=name, url=url, product_list=product_list))
    return section_list


def parse_product(url):
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


def get_html_data(url):
    cookies = dict(region='1')
    try:
        html = requests.get(url, cookies=cookies)
    except Exception as exc:
        print(exc)
    else:
        try:
            html_data = BeautifulSoup(html.text, "lxml")
        except Exception as exc:
            print(exc)
        else:
            return html_data


def check_sections_existence(url):
    html_data = get_html_data(url=url)
    try:
        tag = (html_data.find('span', {'class': "xf-filter__header-text js-shave-container"}))
        if tag.get_text(strip=True) == 'Разделы':
            return True
        else:
            return False
    except AttributeError:
        return False
