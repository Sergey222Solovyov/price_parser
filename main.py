from bs4 import BeautifulSoup
from url import perekrestok_url
from utils import time_track
from functions import get_html, get_catalog, complete_url_fullness


@time_track
def main():
    html_page = BeautifulSoup(get_html(url=perekrestok_url), "lxml")
    catalog_list = get_catalog(html_page)

    print("d")


if __name__ == '__main__':
    main()
