from get_html import get_html_data
from settings import PRODUCT_CARD, PRODUCT_NAME, PRICE, IS_AVAILABLE


def get_product(url):
    product = Product(url)
    product.set_product_data()
    return product


class Product:
    def __init__(self, url, name="None", price="None", available=False):
        self.url = url
        self.name = name
        self.price = price
        self.available = available
        self.error_free = True

    def set_name(self):

        tag_name = self.html_data.find('div', {'class': PRODUCT_CARD})
        self.name = tag_name.get(PRODUCT_NAME)

    def set_is_available(self):
        if self.error_free:
            tag = self.html_data.find('div', {'class': PRODUCT_CARD})
            if tag.get(IS_AVAILABLE) == "1":
                self.available = True
            else:
                self.available = False

    def set_price(self):
        tag_price = self.html_data('span', {'class': PRICE})
        for tag in tag_price:
            if tag.get("itemprop") == "price":
                self.price = tag.get_text()
                break
        if self.price == "None" and self.available:
            self.error_free = False

    def set_html_data(self):
        self.html_data = get_html_data(self.url)
        self.error_check()

    def set_product_data(self):
        self.set_html_data()
        self.error_check()
        if self.error_free:
            self.set_name()
            self.set_is_available()
            self.set_price()

    def error_check(self):
        try:
            self.error_free = False
            tag = self.html_data.find('div', {'class': PRODUCT_CARD})
            tag.get("itemprop")
            tag.get(PRODUCT_NAME)
        except AttributeError:
            print("По данному URL: {} ничего не найдено. \nНазвание Продукта: {}".format(self.url, self.name))
        except TypeError as exe:
            print("{}, {}".format(exe, self.name))
        else:
            self.error_free = True
