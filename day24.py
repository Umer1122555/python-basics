from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
driver.maximize_window()

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# 1. Get all products
products = driver.find_elements(By.CLASS_NAME, "inventory_item")
print(f"Total products found: {len(products)}")

# 2. ASSERT - The main QA check
try:
    assert len(products) == 6, f"FAIL: Expected 6 products but found {len(products)}"
    print("PASS: Product count is correct")
    test_result = "PASS"
except AssertionError as e:
    print(e)
    test_result = "FAIL"

# 3. Print all product names
for i, product in enumerate(products, 1):
    name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
    print(f"Product {i}: {name}")

# 4. SCREENSHOT - Take evidence
driver.save_screenshot("saucedemo_products.png")
print("Screenshot saved as saucedemo_products.png")

# 5. REPORT.TXT - Save result in file
with open("selenium_report.txt", "w") as f:
    f.write(f"Test Name: Product Count Check\n")
    f.write(f"Result: {test_result}\n")
    f.write(f"Total Products Found: {len(products)}\n")
print("Report saved as selenium_report.txt")

driver.quit()