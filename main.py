from update import update_prices
from settings import FILE, FILE_DUPLICATE
from utils import time_track


@time_track
def main():
    update_prices(origin_file=FILE, duplicate_file=FILE_DUPLICATE)


if __name__ == '__main__':
    main()
