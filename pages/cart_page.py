from selenium.webdriver.common.by import By
from pages.base_page import Page




class CartPage(Page):
        cart_empty_txt = 'your cart is empty'
        TEXT_CART_EMPTY = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
        CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
        CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]")
        CART_ITEM = (By.CSS_SELECTOR, "[data-test='cartItem']")

        def verify_cart_opened(self):
             self.driver.get('https://www.target.com/cart')

        def verify_cart_is_empty(self):
            actual_text = self.find_element(*self.TEXT_CART_EMPTY).text
            assert "Your cart is empty" in actual_text, f'Error! text "Your cart is empty" not in {actual_text}'

        def verify_product_name(self, product):
            actual_name = self.driver.find_element(*self.CART_ITEM_TITLE).text
            assert product in actual_name, f'Expected {product} did not match actual {actual_name}'

        def verify_cart_items(self, amount):
            amount = int(amount)
            items = self.driver.find_elements(By.CSS_SELECTOR, '[data-test="cart-item"]')  # adjust selector
            actual_count = len(items)
            assert actual_count == amount, f'Expected {amount} item(s), but found {actual_count}'



