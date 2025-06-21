
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#opens Target website
driver.get("https://www.Target.com")

driver.find_element(By.XPATH,"//a[@aria-label='Account, sign in']").click()


sleep(3)

driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(3)


expected_result = "Sign in with password"
actual_result = driver.find_element(By.ID, "login").text

driver.quit()

