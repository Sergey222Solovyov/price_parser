import time
import re

PEREKRESTOK_URL = 'https://www.perekrestok.ru'
needless_catalogs = ["Скидки", "Сейчас актуально", "Зоотовары"]


def complete_url_fullness(url):
    if re.search(r'\bhttps\b', url) or re.search(r'\bhttp\b', url):
        return url
    else:
        return PEREKRESTOK_URL + url


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'The function worked for {elapsed / 60} min')
        return result

    return surrogate
