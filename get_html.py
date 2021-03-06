import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth


def get_html_data(url):
    cookies = dict(region='1')
    try:
        header = {

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0)   Gecko/20100101 Firefox/69.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'ru,en-US;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'}

        html = requests.get(url, cookies=cookies, headers=header)

        html_data = BeautifulSoup(html.text, "lxml")
    except Exception as exc:
        print(exc)
    else:
        return html_data
