import requests
from bs4 import BeautifulSoup


def get_html_data(url):
    cookies = dict(region='1')
    try:
        html = requests.get(url, cookies=cookies)
        html_data = BeautifulSoup(html.text, "lxml")
    except Exception as exc:
        print(exc)
    else:
        return html_data
