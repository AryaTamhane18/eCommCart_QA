from utils.logger import log


class CartPage:
    locators = {
        "ADD_TO_CART_BUTTON": "//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button",
        "CART_BADGE": "span.shopping_cart_badge",
        "CART_ICON": ".shopping_cart_link",
        "SELECT_SORT_DROPDOWN": "select[data-test='product-sort-container']",
        "PRODUCTS_PAGE": "span.title",
        "PRODUCT_PRICE": "div.inventory_item_price",
        "REMOVE_ITEM": "//button[contains(@id,'remove-')]"
    }

    def __init__(self, page):
        self.page = page

    def add_item_to_cart(self, item):
        product_selector = self.locators["ADD_TO_CART_BUTTON"].format(item_name=item)
        self.page.click(product_selector)

    def go_to_cart(self):
        self.page.click(self.locators["CART_ICON"])

    def remove_item(self):
        remove_item = self.page.locator(self.locators["REMOVE_ITEM"])
        if remove_item.count() > 0:
            remove_item.nth(0).click()

    def get_cart_badge_count(self):
        return self.page.locator(self.locators["CART_BADGE"]).is_visible()

    def select_sort_option(self, option_text):
        self.page.select_option(self.locators["SELECT_SORT_DROPDOWN"], label=option_text)

    def user_is_on_products_page(self):
        return self.page.locator(self.locators["PRODUCTS_PAGE"]).inner_text()

    def verify_sorting_order(self):
        prices_raw = self.page.locator(self.locators["PRODUCT_PRICE"]).all_inner_texts()
        prices = [float(price.replace("$", "")) for price in prices_raw]
        sorted_asc = sorted(prices)
        sorted_desc = sorted(prices, reverse=True)

        if prices == sorted_asc:
            log.info("Products are sorted in ascending order.")
        elif prices == sorted_desc:
            log.info("Products are sorted in descending order.")
        else:
            raise AssertionError("Products are not sorted correctly.")








