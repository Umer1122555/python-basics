from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
driver.maximize_window()

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# DAY 25: SMART WAIT 
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
    print("PASS: Products page loaded")
    test_result = "PASS"
except:
    print("FAIL: Products page did not load in 10 seconds")
    driver.save_screenshot("day25_fail.png")
    test_result = "FAIL"

# Get product count
products = driver.find_elements(By.CLASS_NAME, "inventory_item")
print(f"Products found: {len(products)}")

driver.quit()