from functions import get_catalog
from utils import time_track


@time_track
def main():
    catalog = get_catalog("https://www.perekrestok.ru/")


if __name__ == '__main__':
    main()
