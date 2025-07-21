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

#Step 1
# definiskan si product link dulu
product_link = driver.find_element(By.XPATH, '//a[@data-product-id="1"]')

#scroll dulu baru klik 
driver.execute_script("arguments[0].scrollIntoView();", product_link)
product_link.click()

print("Berhasil melihat prodyuct (view product detail)!")

#Step 2  - write review lh
#definisikan si name_input dulu biar kebaca
name_input = driver.find_element(By.ID, "name")
driver.execute_script("arguments[0].scrollIntoView();", name_input)

name_input.send_keys("Budi")
driver.find_element(By.ID, "email").send_keys("budi@gmail.com")
driver.find_element(By.ID, "review").send_keys("Bajunya bagus deh keknya")
driver.find_element(By.ID, "button-review").click()

print("Berhasil menambahkan review deh")

driver.quit()
