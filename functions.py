import requests
import re
from bs4 import BeautifulSoup
from clases import Catalog, SubCatalog, Section, Product
from url import perekrestok_url
from utils import needless_catalogs


def get_product(url):
    next_url = url + "?page=1"
    product_list = []
    products_exist = True
    while products_exist:
        products_exist = False
        html_data = get_html_data(url=next_url)
        for tag in (html_data('div', {'class': "xf-product js-product"})):
            name = tag.get('data-owox-product-name')
            price = tag.get('data-owox-product-price')
            url = complete_url_fullness(tag.get('data-product-card-url'))
            product_list.append(Product(name=name, price=price, url=url))
            products_exist = True
        try:
            next_url = complete_url_fullness(
                (html_data.find('a', {'class': "xf-paginator__item js-paginator__next"})).get('href'))
        except AttributeError:
            products_exist = False
    return product_list


def get_section(url):
    section_list = []
    html_data = get_html_data(url=url)
    for tag in (html_data('a', {'class': "xf-filter__item-label xf-ripple js-xf-ripple xf-ripple_gray"})):
        url = complete_url_fullness(tag.get('href'))
        name = tag.get_text(strip=True)
        product_list = get_product(url=url)
        section_list.append(Section(name=name, url=url, product_list=product_list))
    return section_list


def get_sub_catalog(html_data, catalog_id):
    sub_catalog = []
    for tag in (html_data.find_all('a', {'data-id': catalog_id})):
        name = tag.get_text()
        url = complete_url_fullness(tag.get('href'))
        sections_exist = check_sections_existence(url=url)
        if sections_exist:
            section_list = get_section(url=url)
            sub_catalog.append(SubCatalog(name=name, url=url, section_list=section_list))
        else:
            product_list = get_product(url)
            section_list = [Section(name=name, url=url, product_list=product_list)]
            sub_catalog.append(SubCatalog(name=name, url=url, section_list=section_list))
    return sub_catalog


def get_catalog(url):
    html_data = get_html_data(url=url)
    catalog_list = []
    for tag in (html_data('a', {'class': "fo-catalog-menu__nav-link"})):
        name = tag.get_text()
        if re.search(name, needless_catalogs):
            continue
        else:
            sub_catalog_list = get_sub_catalog(catalog_id=tag.get('data-category-id'), html_data=html_data)
            catalog_list.append(Catalog(name=name, sub_catalog_list=sub_catalog_list))
    return catalog_list


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


def complete_url_fullness(url):
    if re.search(r'\bhttps\b', url) or re.search(r'\bhttp\b', url):
        return url
    else:
        return perekrestok_url + url


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
