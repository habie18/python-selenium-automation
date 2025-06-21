

# Amazon logo
driver.find_element(By.CSS_SELECTOR, '[aria-label="Amazon"]')
# Create Account text
driver.find_element(By.XPATH, '//h1[@class="a-spacing-small"]')
# Name input field
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
# Mobile number / Email input field
driver.find_element(By.CSS_SELECTOR, '#ap_email')
# Password input field
driver.find_element(By.CSS_SELECTOR, '#ap_password')
# Password input field helper text
driver.find_element(By.XPATH, '.a-alert-inline-info')
# Re-enter password input field
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
# Continue button
driver.find_element(By.CSS_SELECTOR, '#continue')
# Conditions of Use link
driver.find_element(By.CSS_SELECTOR, '[href*="condition"]')
# Privacy Notice link
driver.find_element(By.CSS_SELECTOR, '[href*="register_notification_privacy"]')
# Sign in link
driver.find_element(By.CSS_SELECTOR, '[href*="signin"]')