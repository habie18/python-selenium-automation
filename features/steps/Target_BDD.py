from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then, given

@given('Open target cart')
def open_main_page(context):
    context.driver.get("https://www.target.com/cart")



@then('verify empty cart')
def verify_empty_cart(context):
  context.app.cart_page.verify_empty_cart()



@when('Click on Sign in')
def click_sign_in(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="@web/AccountLink"]'))
    ).click()

@when('Click Sign in on side menu')
def click_side_menu_sign_in(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="accountNav-signIn"]'))
    ).click()

@then('Verify Sign in form opens')
def verify_sign_in_form(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#login'))
    )

