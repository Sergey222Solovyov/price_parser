import requests
import re
from bs4 import BeautifulSoup
from clases import Catalog, SubCatalog, Section, Product
from url import perekrestok_url
from utils import needless_catalogs


def get_product_values(html_data, product_list):
    product_exists = False
    for tag in (html_data('div', {'class': "xf-product js-product"})):
        name = tag.get('data-owox-product-name')
        price = tag.get('data-owox-product-price')
        url = complete_url_fullness(
            (html_data.find('a', {'class': "xf-product-picture__link js-product__image"})).get('href'))
        product_list.append(Product(name=name, price=price, url=url))
        product_exists = True
    return product_exists


def get_product(url):
    PAGE = '?page='
    i = 2
    product_list = []
    html_data = BeautifulSoup(get_html(url=url), "lxml")
    product_exists = get_product_values(html_data, product_list)

    while product_exists:
        url_with_page = url + PAGE + str(i)
        html_data = BeautifulSoup(get_html(url=url_with_page), "lxml")
        try:
            href = html_data.find('link', {'rel': "canonical"}).get('href')
        except AttributeError:
            href = url_with_page
        if url_with_page == href:
            product_exists = get_product_values(html_data, product_list)
            i += 1
        else:
            product_exists = False

    return product_list


def get_section(url):
    section_list = []
    html_data = BeautifulSoup(get_html(url=url), "lxml")
    for tag in (html_data('a', {'class': "xf-filter__item-label xf-ripple js-xf-ripple xf-ripple_gray"})):
        url = complete_url_fullness(tag.get('href'))
        name = tag.get_text(strip=True)
        product_list = get_product(url)
        section_list.append(Section(name=name, url=url, product_list=product_list))
    return section_list


def get_sub_catalog(catalog_id, html_data):
    sub_catalog = []

    for tag in (html_data.find_all('a', {'data-id': catalog_id})):
        name = tag.get_text()
        url = complete_url_fullness(tag.get('href'))
        section_exist = check_section_existence(url)
        if section_exist:
            section_list = get_section(url=url)
            sub_catalog.append(SubCatalog(name=name, url=url, section_list=section_list))
        else:
            section_list = [Section(name=name, url=url)]
            sub_catalog.append(SubCatalog(name=name, url=url, section_list=section_list))

    return sub_catalog


def get_catalog(html_data):
    catalog_list = []
    for tag in (html_data('a', {'class': "fo-catalog-menu__nav-link"})):
        name = tag.get_text()
        if re.search(name, needless_catalogs):
            continue
        sub_catalog_list = get_sub_catalog(catalog_id=tag.get('data-category-id'), html_data=html_data)
        catalog_list.append(Catalog(name=name, sub_catalog_list=sub_catalog_list))
    return catalog_list


def get_html(url):
    cookies = dict(region='1')
    try:
        html = requests.get(url, cookies=cookies)
    except Exception as exc:
        print(exc)
    else:
        return html.text


def complete_url_fullness(url):
    if re.search(r'\bhttps\b', url):
        return url
    else:
        return perekrestok_url + url


def check_section_existence(url):
    html_data = BeautifulSoup(get_html(url=url), "lxml")
    tag = (html_data('span', {'class': "xf-filter__header-text js-shave-container"}))
    try:
        if tag[0].get_text(strip=True) == 'Разделы':
            return True
        else:
            return False
    except IndexError:
        return False
