from file import get_product_list_from_file, rewrite_file, add_product_to_file


def update_prices(file):
    product_list = get_product_list_from_file(file)
    rewrite_file(file)
    for product in product_list:
        old_price = product.price
        update_availability(product)
        if product.is_available:
            product.set_price()
            if old_price != product.price:
                print(
                    "Цена на товар: '{}' изменилась с '{}' RUB на '{}' RUB".format(product.name, old_price,
                                                                                   product.price))

        add_product_to_file(product, file)


def update_availability(product):
    if product.is_available:
        product.set_html_data()
        product.set_is_available()
        if not product.is_available:
            print("Товар: '{}' временно отсутствует".format(product.name))
    else:
        product.set_html_data()
        product.set_is_available()
        if product.is_available:
            print("Товар: '{}' теперь доступен.".format(product.name, product.price))
