import tempfile
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait





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

    # 3. Go to cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)

    # 4. Checkout
    checkout_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_btn.click()

    # 5. Fill details
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    time.sleep(1)

    # 6. Finish
    driver.find_element(By.ID, "finish").click()
    time.sleep(2)

    success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert success_message == "Wrong text"