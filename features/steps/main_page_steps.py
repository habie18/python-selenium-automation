from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep





@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main_page()


