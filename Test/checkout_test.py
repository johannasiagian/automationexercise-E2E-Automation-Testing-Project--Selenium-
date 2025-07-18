import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 
from selenium import webdriver
from selenium.webdriver.common.by import By
from Helpers.login_helper import do_login


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationexercise.com/login")

do_login(driver,"andikawowsekali123@gmail.com", "andikawowsekali123")

time.sleep(3)

driver.find_element(By.CSS_SELECTOR, 'a[href="/view_cart"]').click()

driver.find_element(By.CSS_SELECTOR, "#do_action > div.container > div > div > a").click()
driver.find_element(By.CSS_SELECTOR, "#cart_items > div > div:nth-child(7) > a").click()

#Step 2 - Fill Payment

driver.find_element(By.CSS_SELECTOR, "#payment-form > div:nth-child(2) > div > input").send_keys("AndikaPutra")
driver.find_element(By.CSS_SELECTOR, "#payment-form > div:nth-child(3) > div > input").send_keys("378282246310005")
driver.find_element(By.CSS_SELECTOR, "#payment-form > div:nth-child(4) > div.col-sm-4.form-group.cvc > input").send_keys("311")
driver.find_element(By.CSS_SELECTOR, "#payment-form > div:nth-child(4) > div:nth-child(2) > input").send_keys("05")
driver.find_element(By.CSS_SELECTOR, "#payment-form > div:nth-child(4) > div:nth-child(3) > input").send_keys("2027")
driver.find_element(By.CSS_SELECTOR, "#submit").click()

print("Berhasil melakukan checkoout nih!")

driver.quit()


