import csv


def update_file(file_name):
    with open(file_name, mode='w', newline='', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Name", "Price", "URL"])
    return file_name


def add_product_to_file(product, file_name):
    with open(file_name, mode='a', newline='', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';')
        try:
            writer.writerow([product[0], product[1], product[2]])
        except IndexError:
            pass


def get_product_list_from_file(file_name):
    product_list = []
    try:
        with open(file_name, mode='r', newline='', encoding='cp1251') as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                product_dict = {'Name': row['Name'], 'Price': row['Price'], 'URL': row['URL']}
                product_list.append(product_dict)
    except FileNotFoundError:
        print("Файл с данным именем не найден.")
        return []
    return product_list
