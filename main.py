import requests
import typing
from bs4 import BeautifulSoup
from url import perekrestok_url


class Subdirectory:
    pass


class SubLink:
    def __init__(self, name, url):
        self.url = url
        self.name = name


class CatalogMenu:
    def __init__(self, name, subdirectory_list: typing.List[SubLink]):
        self.name = name
        self.subdirectory_list = subdirectory_list


def get_text(url):
    html = requests.get(url, auth=('user', 'pass'))
    text = html.text
    return text


def get_catalog_menu(html_page):
    catalog_menu_list = []
    for category in (html_page.find_all('a', {'class': "fo-catalog-menu__nav-link"})):
        catalog_menu_list.append(CatalogMenu(name=category.get_text(), subdirectory_list=get_sub_link(
            catalog_id=category.get('data-category-id'), html_page=html_page)))
    return catalog_menu_list


def get_sub_link(catalog_id, html_page):
    sub_links = []
    for sub_link in (html_page.find_all('a', {'class': "fo-catalog-menu__sub-link"})):
        if catalog_id == sub_link.get('data-id'):
            sub_links.append(
                SubLink(name=sub_link.get_text(), url=("https://www.perekrestok.ru" + sub_link.get('href'))))
    return sub_links


def main():
    html_page = BeautifulSoup(get_text(url=perekrestok_url), "lxml")





if __name__ == '__main__':
    main()
