import csv

from Product import Product


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
            print("Не удалось записать данный товар в файл")


def get_products_list_from_file(file):
    products_list = []
    try:
        with open(file, mode='r', newline='', encoding='cp1251') as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                products_list.append(Product(name=row['Name'], price=row['Price'], url=row['URL'],
                                             is_available=bool(row['Is available'])))
    except FileNotFoundError:
        print("Файл с данным именем не найден.")
        return []
    return products_list
