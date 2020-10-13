import time

from settings import PEREKRESTOK_URL


def convert_str_to_bool(string):
    if string == "True" or string == "TRUE":
        return True
    else:
        return False


def complete_url_fullness(url):
    if 'http' in url:
        return url
    else:
        return PEREKRESTOK_URL + url


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'The function worked for {elapsed} sec')
        return result

    return surrogate
