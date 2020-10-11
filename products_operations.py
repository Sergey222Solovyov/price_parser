from get_html import get_html_data
from settings import PRODUCT_CARD, PRICE_LINK, PRODUCT_NAME, PRICE


def get_product(url):
    html_data = get_html_data(url=url)
    product = []
    try:
        tag_name = html_data.find('div', {'class': PRODUCT_CARD})
        tag_price = html_data.find('span', {'class': PRICE_LINK})
        name = tag_name.get(PRODUCT_NAME)
        price = tag_price.get(PRICE)
        product.append(name)
        product.append(price)
        product.append(url)
    except AttributeError:
        print("По данному URL ничего не найдено.")
        return []
    else:
        return product