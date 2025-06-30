from behave import *
from Pages.login_page import LoginPage
from utils.env import get_env_variable

use_step_matcher("re")


@given("the user navigates to login page")
def step_navigate_to_login_page(context):
    context.page.wait_for_timeout(1000)


@when("the user enters username (?P<username>.+) and password")
def step_enter_username_and_password(context, username):
    password = get_env_variable("PASSWORD")
    context.login = LoginPage(context.page)
    context.login.fill_login(username, password)


@then("the user should see the products page")
def step_check_user_is_on_products_page(context):
    context.login.verify_on_products_page()








