from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Open Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Go to the site
driver.get("https://www.saucedemo.com")

# Type into username and password boxes
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Click login
driver.find_element(By.ID, "login-button").click()

time.sleep(2)  # just so you can SEE it worked

# Check we landed on the right page
if "inventory" in driver.current_url:
    print("✅ Login test PASSED")
else:
    print("❌ Login test FAILED")

driver.quit()