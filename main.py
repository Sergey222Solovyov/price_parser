from Product import get_product
from file import add_product_to_file
from update import update_product_list
from settings import FILE, DUPLICATE_FILE
from utils import time_track


def add_product(url):
    product = get_product(url)
    if add_product_to_file(product, FILE):
        print("Товар успешно добавлен в файл! ")


@time_track
def main():


    # add_product(input())
    update_product_list(origin_file=FILE, duplicate_file=DUPLICATE_FILE)


if __name__ == '__main__':
    main()
