from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainPage(Page):
    SEARCH_FIELD =(By.ID, 'search')


    def open_main_page(self):
        self.driver.get('https://www.target.com/')


