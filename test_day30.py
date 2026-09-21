import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()

def test_full_checkout_flow(driver):
    wait = WebDriverWait(driver, 10)
    
    # 1. Login
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # 2. Add to Cart
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    
    # 3. Go to Cart
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
    
    # 4. Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    
    # 5. Finish
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
    
    # 6. Assert
    success_msg = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))).text
    assert "Thank you" in success_msg