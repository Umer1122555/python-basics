
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--user-data-dir=C:\\temp\\chrome-profile")
        d = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        options.add_argument("--headless")
        d = webdriver.Firefox(options=options)
    yield d
    d.quit()


def test_checkout_flow(driver):
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

    checkout_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "checkout"))
)
    checkout_btn.click()
    
    


    checkout_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "checkout"))
)
checkout_btn.click()

    
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    time.sleep(1)

    
    driver.find_element(By.ID, "finish").click()
    time.sleep(2)

    
    success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert success_message == "Thank you for your order!"
