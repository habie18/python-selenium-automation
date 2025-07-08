from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")


@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main_page()

@when('Click on Add to Cart')
def click_add_cart(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(ADD_TO_CART_BTN)
    ).click()











#@when('Search for {product}')
#def search_product(context, product):
 #   print(product)
  #  context.driver.find_element(By.ID, 'search').send_keys('tea')
   # context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    #sleep(9)
    #context.app.header.search_product(product)
    #print(product)
    #context.driver.find_element(By.ID, 'search').send_keys('tea')
    #context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    #sleep(9)
