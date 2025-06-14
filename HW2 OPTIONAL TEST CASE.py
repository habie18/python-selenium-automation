from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


# open the url
driver.get('https://www.target.com/')

# Locate and populate the Search bar
driver.find_element(By.ID, 'search').send_keys('Bicycle')


sleep(4)

# click on Search icon
driver.find_element(By.XPATH, "//button[@aria-label='search']").click()


sleep(4)

# Verification process
#expected_result = 'results'
#actual_result = driver.find_element(By.XPATH, "//div[@data-test='results-facets-row']").text

#assert expected_result in actual_result, f"Expected to find {expected_result}, got {actual_result}"
assert 'Bicycle' .lower() in driver.current_url.lower() , f"Expected query not in {driver.current_url.lower()}"


print("Test passed")



driver.quit()