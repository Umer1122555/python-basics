from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Browser open
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # Step 1: Login to Saucedemo
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("Step 1: Login successful")

    # Step 2: WAIT + Use CSS_SELECTOR to find page title
    title_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".title")))
    title = title_element.text

    # Step 3: ASSERTION 1 - Did we land on Products page?
    assert title == "Products", f"Expected 'Products' but got '{title}'"
    print("Assertion 1 Passed: On Products Page ✅")

    # Step 4: Use XPATH to find all products and ASSERTION 2
    products = driver.find_elements(By.XPATH, "//div[@class='inventory_item']")
    assert len(products) == 6, f"Expected 6 products but found {len(products)}"
    print(f"Assertion 2 Passed: Found {len(products)} products ✅")

    print("\nDay 26 DONE! All tests passed 🔥")

except AssertionError as e:
    print(f"\nTest FAILED: {e}")
    
finally:
    # 5 sec ruk kar browser band
    import time
    time.sleep(5)
    driver.quit()