import threading

from file import get_product_list_from_file, rewrite_file, add_product_to_file, overwrite_origin_file


def update_product_list(origin_file, duplicate_file):
    product_list = get_product_list_from_file(origin_file)
    product_thread_list = []
    rewrite_file(file=duplicate_file)
    for product in product_list:
        product_thread = threading.Thread(target=update_product, args=(product, duplicate_file))
        product_thread_list.append(product_thread)
        product_thread.start()
    for product_thread in product_thread_list:
        product_thread.join()
    overwrite_origin_file(origin_file=origin_file, duplicate_file=duplicate_file)


def update_product(product, duplicate_file):
    product.set_html_data()
    if product.error_free:
        old_price = product.price
        update_availability(product)
        if product.available:
            product.set_price()
            if old_price != product.price:
                print(
                    "Цена на товар: '{}' изменилась с '{}' RUB на '{}' RUB".format(product.name, old_price,
                                                                                   product.price))
    else:
        product.error_free = True
    add_product_to_file(product, duplicate_file)


def update_availability(product):
    if product.available:
        product.set_is_available()
        if not product.available:
            print("Товар: '{}' временно отсутствует".format(product.name))
    else:
        product.set_is_available()
        if product.available:
            print("Товар: '{}' теперь доступен.".format(product.name, product.price))
