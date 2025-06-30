import time
from pathlib import Path
from behave import *

from Pages.products_page import ProductsPage
import json
use_step_matcher("re")


@when("user adds all items to the cart from json file")
def step_add_all_items_from_json_file(context):
    context.products_page = ProductsPage(context.page)
    path = Path(__file__).parents[2] / "tests" / "test_data" / "products.json"

    with open(path, 'r') as file:
        context.product_data = json.load(file)

    for product in context.product_data:
        context.products_page.add_product_to_cart(product['id'])
        time.sleep(3)
    context.products_page.click_on_cart_icon()
    time.sleep(5)


@then("the user should see those items in the cart with correct names and prices")
def step_validate_cart_items(context):
    cart_items = context.products_page.get_cart_item_names()
    expected_items = context.product_data
    assert len(cart_items) == len(expected_items), "Cart items count does not match expected count"

    for i in range(len(expected_items)):
        assert expected_items[i]["name"] == cart_items[i]["name"], "Name mismatch"
        assert expected_items[i]["price"] == cart_items[i]["price"], "Price mismatch"



