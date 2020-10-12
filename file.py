import csv


def update_file(file):
    with open(file, mode='w', newline='', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Name", "Price", "URL"])
    return file


def add_product_info_to_file(product_info, file):
    with open(file, mode='a', newline='', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';')
        try:
            writer.writerow([product_info[0], product_info[1], product_info[2]])
        except IndexError:
            pass


def get_products_list_from_file(file):
    products_list = []
    try:
        with open(file, mode='r', newline='', encoding='cp1251') as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                product_dict = {'Name': row['Name'], 'Price': row['Price'], 'URL': row['URL']}
                products_list.append(product_dict)
    except FileNotFoundError:
        print("Файл с данным именем не найден.")
        return []
    return products_list
