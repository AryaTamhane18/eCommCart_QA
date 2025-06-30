class ProductsPage:
    locators = {
        "ADD_TO_CART_BUTTON_TEMPLATE": "button[data-test='add-to-cart-{id}']",
        "CART_ICON": ".shopping_cart_link",
        "CART_ITEM_NAMES": ".inventory_item_name",
        "CART_ITEM_PRICES": ".inventory_item_price",

    }

    def __init__(self, page):
        self.page = page

    def add_product_to_cart(self, product_id):
        button_locator = self.locators["ADD_TO_CART_BUTTON_TEMPLATE"].format(id=product_id)
        self.page.click(button_locator)

    def click_on_cart_icon(self):
        self.page.click(self.locators["CART_ICON"])

    def get_cart_item_names(self):
        names = self.page.locator(self.locators["CART_ITEM_NAMES"]).all_inner_texts()
        prices = self.page.locator(self.locators["CART_ITEM_PRICES"]).all_inner_texts()
        return [{'name': name, 'price': price} for name, price in zip(names, prices)]





