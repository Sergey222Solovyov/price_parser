import csv

from file_operations import get_product_list_from_file, update_file
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


def check_prices(file_name):
    product_list = get_product_list_from_file(file_name)
    update_file(file_name)
    with open(file_name, mode='a', newline='', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';')
        for product in product_list:
            new_price = get_price(product['URL'])
            if prices_equal(old_price=product['Price'], new_price=new_price):
                pass
            else:
                print("Цена на {} изменилась с {} на {}".format(product['Name'], product['Price'], new_price))
            writer.writerow([product['Name'], new_price, product['URL']])


def prices_equal(old_price, new_price):
    if old_price == new_price:
        return True
    else:
        return False
