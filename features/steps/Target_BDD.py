from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target')
def open_main_page(context):
    context.driver.get("https://www.target.com/")

@when('click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartIcon"]').click()
    sleep(5)

@then('verify empty cart')
def verify_empty_cart(context):
    actual_text=context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]').text
    expected_text="Your cart is empty"
    assert actual_text == expected_text, f"error, expected {expected_text}, but got actual {actual_text}"
    sleep(5)



@when('Click on Sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/AccountLink"]').click()
    sleep(2)


@when('Click Sign in on side menu')
def click_side_menu_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="accountNav-signIn"]').click()
    sleep(2)


@then('Verify Sign in form opens')
def verify_sign_in_form(context):
    context.driver.find_element(By.CSS_SELECTOR, '#login')
    sleep(4)

