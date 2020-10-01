import requests

from clases import Catalog, SubCatalog, Section


def get_section(html_page):
    section_list = []
    for link in (html_page('a', {'class': "xf-filter__item-label xf-ripple js-xf-ripple xf-ripple_gray"})):
        section_list.append(Section(name=link.get_text, url=(check_url(link.get('href')))))
    return section_list


def get_sub_catalog(catalog_id, html_page):
    sub_catalog = []
    for link in (html_page('a', {'class': "fo-catalog-menu__sub-link"})):
        if catalog_id == link.get('data-id'):
            sub_catalog.append(
                SubCatalog(name=link.get_text(), url=(check_url(link.get('href')))))
    return sub_catalog


def get_catalog(html_page):
    catalog_list = []
    for link in (html_page('a', {'class': "fo-catalog-menu__nav-link"})):
        catalog_list.append(Catalog(name=link.get_text(), sub_catalog_list=get_sub_catalog(
            catalog_id=link.get('data-category-id'), html_page=html_page)))
    return catalog_list


def get_html(url):
    html = requests.get(url, auth=('user', 'pass'))
    return html.text


def check_url(url):
    http = "http"
    for _ in range(len(http)):
        if http[_] != url[_]:
            return "https://www.perekrestok.ru" + url
    return url
