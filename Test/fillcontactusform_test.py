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

do_login(driver, "andikawowsekali123@gmail.com", "andikawowsekali123")

time.sleep(3)

driver.find_element(By.CSS_SELECTOR, 'a[href="/contact_us"]').click()

driver.find_element(By.CSS_SELECTOR, "#contact-us-form > div:nth-child(2) > input").send_keys("Andika")
driver.find_element(By.CSS_SELECTOR, "#contact-us-form > div:nth-child(3) > input").send_keys("Andikaawkoaw123@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#contact-us-form > div:nth-child(4) > input").send_keys("mantap")
driver.find_element(By.ID, "message").send_keys("Luarbiasa sekali")
driver.find_element(By.CSS_SELECTOR, "#contact-us-form > div:nth-child(6) > input").send_keys("C:/Users/Dian Pramesti/Downloads/keju cheedar.jpeg")
driver.find_element(By.CSS_SELECTOR, "#contact-us-form > div:nth-child(7) > input").click()

print("Berhasiil")

driver.quit()