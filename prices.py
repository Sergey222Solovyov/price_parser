from file_operations import get_products_list_from_file, update_file, add_product_info_to_file
from get_html import get_html_data
from settings import PRICE_LINK, PRICE


def get_price(url):
    html_data = get_html_data(url=url)
    try:
        tag_price = html_data.find('span', {'class': PRICE_LINK})
        price = tag_price.get(PRICE)
    except AttributeError as exc:
        print(exc)
    else:
        return price


def check_prices(file):
    products_list = get_products_list_from_file(file)
    update_file(file)
    for product in products_list:
        new_price = get_price(product['URL'])
        if prices_equal(old_price=product['Price'], new_price=new_price):
            pass
        else:
            print("Цена на товар: {} изменилась с '{}' на '{}'".format(product['Name'], product['Price'], new_price))
        product_info = [product['Name'], new_price, product['URL']]
        add_product_info_to_file(product_info, file)


def prices_equal(old_price, new_price):
    if old_price == new_price:
        return True
    else:
        return False
