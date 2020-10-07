from get_lists import get_catalog_list
from utils import time_track


@time_track
def main():
    catalog_list = get_catalog_list()


if __name__ == '__main__':
    main()
