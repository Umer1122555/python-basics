from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
def test_checkout_flow():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    
    # 1. Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    
    # 2. Add all 6 items
    add_buttons = driver.find_elements(By.CSS_SELECTOR, "button.btn_inventory")
    for button in add_buttons:
        button.click()
    time.sleep(1)
    
    # 3. Go to Cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)
    
    # 4. Click Checkout
    driver.find_element(By.ID, "checkout").click()
    time.sleep(1)
    
    # 5. Fill Checkout Info
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    time.sleep(1)
    
    # 6. Click Finish
    driver.find_element(By.ID, "finish").click()
    time.sleep(2)
    
    # 7. ASSERT - Did we see success message?
    success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert success_message == "Thank you for your order!"
    
    driver.quit()
