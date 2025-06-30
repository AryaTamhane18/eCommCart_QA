from behave import *
from Pages.cart_page import CartPage
from Pages.login_page import LoginPage

use_step_matcher("re")


@given("user has logged in and is now on products page")
def step_user_has_logged_in(context):
    context.login = LoginPage(context.page)
    context.login.fill_login("standard_user", "secret_sauce")
    context.cart = CartPage(context.page)
    products_page = context.cart.user_is_on_products_page()
    assert products_page == 'Products', "User is not on products page after login"


@step("user sorts the products by (?P<option>.+)")
def step_user_sorts_by_option(context, option):
    context.cart = CartPage(context.page)
    context.cart.select_sort_option(option)
    context.page.wait_for_timeout(500)


@then("user validates the order")
def step_user_validates_order(context):
    context.cart.verify_sorting_order()


@when("the user adds an (?P<item>.+) in the cart")
def step_add_an_item_to_cart(context, item):
    context.cart = CartPage(context.page)
    context.cart.add_item_to_cart(item)
    context.page.wait_for_timeout(500)


@then("cart badge should contain the expected count")
def step_verify_cart_badge(context):
    assert context.cart.get_cart_badge_count(), "Cart badge is not visible — item was not added"


@step("user navigates to the cart")
def step_go_to_cart(context):
    context.cart.go_to_cart()


@when("user removes an item from cart")
def step_remove_an_item(context):
    context.cart.remove_item()
    context.page.wait_for_timeout(500)


@then("the cart badge should not be visible")
def step_cart_badge_disappears(context):
    assert not context.cart.get_cart_badge_count(), "cart badge visible after removing item.."
