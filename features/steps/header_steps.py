from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')


@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search_product(search_word)

@when('Click Sign in')
def click_sign_in(context):
    # context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
    #context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
        context.app.header.click_sign_in()
sleep(3)

@when('From right side navigation menu, click Sign in')
def click_right_side_nav_sign_in(context):
        context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
        context.app.header.click_right_side_nav_sign_in()
        #context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()
    context.app.header.click_cart()



@then('Verify header has {number} links')
def verify_header_links(context, number):
    print(type(number))
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)

    # 6 == 6
    assert len(links) == int(number), f'Expected {number} links but got {len(links)}'


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # sleep(2)
    # context.driver.execute_script("window.scrollBy(0,1000)", "")
    # sleep(2)

    products = context.driver.find_elements(*LISTINGS)[:8]  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)