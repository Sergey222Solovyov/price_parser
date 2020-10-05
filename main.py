from parsing import parse_catalog
from utils import time_track


@time_track
def main():
    catalog_list = parse_catalog()


if __name__ == '__main__':
    main()
