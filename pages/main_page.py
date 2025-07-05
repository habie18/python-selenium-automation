from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainPage(Page):

    def open_main_page(self):
        self.driver.get('https://www.target.com/')

