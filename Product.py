from get_html import get_html_data
from settings import PRODUCT_CARD, PRICE_LINK, PRODUCT_NAME, PRICE, IS_AVAILABLE


class Product:
    def __init__(self, url, name="None", price="None", is_available=False):
        self.url = url
        self.name = name
        self.price = price
        self.is_available = is_available
        self.error_free = True

    def set_name(self):
        try:
            tag_name = self.html_data.find('div', {'class': PRODUCT_CARD})
            self.name = tag_name.get(PRODUCT_NAME)
        except AttributeError:
            print("По данному URL: {} \n ничего не найдено".format(self.url))
            self.error_free = False

    def set_is_available(self):
        if self.error_free:
            tag = self.html_data.find('div', {'class': PRODUCT_CARD})
            if tag.get(IS_AVAILABLE) == "1":
                self.is_available = True

    def set_price(self):
        tag_price = self.html_data('span', {'class': PRICE})
        for tag in tag_price:
            if tag.get("itemprop") == "price":
                self.price = tag.get_text()
                break
        if self.price == "None" and self.is_available:
            self.error_free = False

    def set_product_info(self):
        self.html_data = get_html_data(self.url)
        self.set_name()
        self.set_is_available()
        self.set_price()
