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

driver.find_element(By.CSS_SELECTOR, 'a[href="/delete_account"]').click()
driver.find_element(By.CSS_SELECTOR, "#form > div > div > div > div > a").click()

print("Berhasil hapus akunn deh")

driver.quit()