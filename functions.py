import requests
from bs4 import BeautifulSoup

from clases import Catalog, SubCatalog, Section


def get_section(url):
    section_list = []
    html_data = BeautifulSoup(get_html(url=url), "lxml")
    for tag in (html_data('a', {'class': "xf-filter__item-label xf-ripple js-xf-ripple xf-ripple_gray"})):
        url = complete_url_fullness(tag.get('href'))
        name = tag.get_text(strip=True)
        section_list.append(Section(name=name, url=url))
    return section_list


def get_sub_catalog(catalog_id, html_data):
    sub_catalog = []
    for tag in (html_data('a', {'class': "fo-catalog-menu__sub-link"})):
        if catalog_id == tag.get('data-id'):
            name = tag.get_text()
            url = complete_url_fullness(tag.get('href'))
            section_exist = check_section_existence(complete_url_fullness(tag.get('href')))
            if section_exist:
                section_list = get_section(url=complete_url_fullness(tag.get('href')))
                sub_catalog.append(SubCatalog(name=name, url=url, section_list=section_list))
            else:
                sub_catalog.append(Section(name=name, url=url))

    return sub_catalog


def get_catalog(html_data):
    catalog_list = []
    for tag in (html_data('a', {'class': "fo-catalog-menu__nav-link"})):
        name = tag.get_text()
        sub_catalog_list = get_sub_catalog(catalog_id=tag.get('data-category-id'), html_data=html_data)
        catalog_list.append(Catalog(name=name, sub_catalog_list=sub_catalog_list))
    return catalog_list


def get_html(url):
    cookies = dict(region='1')
    html = requests.get(url, cookies=cookies)
    return html.text


def complete_url_fullness(url):
    http = "http"
    for _ in range(len(http)):
        if http[_] != url[_]:
            return "https://www.perekrestok.ru" + url
    return url


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
