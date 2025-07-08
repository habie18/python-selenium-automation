from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)


    def find_element(self, * locator):
        return self.driver.find_element(*locator)

    def click(self, * locator):
        self.driver.find_element(*locator).click()


    def input_text(self, text, * locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, * locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} not shown in actual {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} not shown in actual {actual_text}'

    def wait_to_be_clickable(self, *locator):
        self.driver.wait.until(
            EC.element_to_be_clickable(*locator),
            message=f'Element by {locator} not clickable'
        )

    def wait_to_be_clickable_click(self, *locator):
        self.driver.wait.until(
            EC.element_to_be_clickable(*locator),
            message=f'Element by {locator} not clickable'
        ).click()


    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        print('Actual URL: ',  actual_url)
        assert expected_url==actual_url, f"Expected {expected_url} did not match {actual_url}"

