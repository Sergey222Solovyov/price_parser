import csv

from Product import Product
from utils import convert_str_to_bool


def rewrite_file(file):
    with open(file, mode='w', newline='', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Name", "Price", "URL", "Is available"])


def add_product_to_file(product, file):
    with open(file, mode='a', newline='', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';')
        if product.error_free:
            writer.writerow([product.name, product.price, product.url, product.is_available])
        else:
            print("Не удалось записать данный товар '{}' в файл.".format(product.name))


def get_product_list_from_file(file):
    product_list = []
    try:
        with open(file, mode='r', newline='', encoding='cp1251') as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                name = row['Name']
                price = row['Price']
                url = row['URL']
                is_available = convert_str_to_bool(string=row['Is available'])
                product_list.append(Product(name=name, price=price, url=url, is_available=is_available))
    except FileNotFoundError:
        print("Файл не найден.")
        return []
    return product_list


def overwrite_origin_file_with_duplicate(origin_file, duplicate_file):
    rewrite_file(origin_file)
    product_list = get_product_list_from_file(duplicate_file)
    for product in product_list:
        add_product_to_file(product, origin_file)
