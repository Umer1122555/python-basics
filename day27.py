from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".title")))

title = driver.find_element(By.CSS_SELECTOR, ".title").text
assert title == "Products", f"Fail: expected products but found '{title}'"
print("Passed")

products = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item']")
assert len(products) == 6, f"Fail: expected 6 but got {len(products)}"
print("Passed")

# ===== DAY 27: LOOP THROUGH PRODUCTS =====
for product in products:
    name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
    print(name)
# =========================================

driver.quit()