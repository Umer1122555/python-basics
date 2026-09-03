from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

products = driver.find_elements(By.CLASS_NAME, "inventory_item")
print(f"Total products found: {len(products)}")

for i, product in enumerate(products, 1):
    name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
    price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"Product {i}: {name} - {price}")

driver.quit()