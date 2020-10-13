from update import update_prices
from settings import FILE
from utils import time_track


@time_track
def main():
    update_prices(FILE)


if __name__ == '__main__':
    main()
