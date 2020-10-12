from get_html import get_html_data
from settings import PRODUCT_CARD, PRICE_LINK, PRODUCT_NAME, PRICE


def get_product_info(url):
    html_data = get_html_data(url=url)
    product_info = []
    try:
        tag_name = html_data.find('div', {'class': PRODUCT_CARD})
        tag_price = html_data.find('span', {'class': PRICE_LINK})
        name = tag_name.get(PRODUCT_NAME)
        price = tag_price.get(PRICE)
        product_info.append(name)
        product_info.append(price)
        product_info.append(url)
    except AttributeError:
        print("По данному URL ничего не найдено.")
        return []
    else:
        return product_info
