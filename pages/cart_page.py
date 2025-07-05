from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    EMPTY_CART_TXT = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')

    def verify_empty_cart(self):
        actual_result = self.find_element(*self.EMPTY_CART_TXT)
        assert actual_result, f'Empty cart text not found'
        expected = 'Your cart is empty'
        actual_result = self.find_element(*self.EMPTY_CART_TXT).text
        assert expected == actual_result, f'Empty cart text "{expected}" not found, showed "{actual_result}" '