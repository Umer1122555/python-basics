from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()

# Open saucedemo
driver.get("https://www.saucedemo.com")
print("Browser opened!")
time.sleep(2)

# Find username field and type
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")

# Find password field and type
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")

# Find login button and click
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

print("Logged in!")
time.sleep(5)  # so we can see the result

# Close browser
driver.quit()