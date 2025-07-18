import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 
from selenium import webdriver
from selenium.webdriver.common.by import By
from Helpers.login_helper import do_login
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationexercise.com/login")

do_login(driver,"andikawowsekali123@gmail.com", "andikawowsekali123")

time.sleep(3)

driver.find_element(By.CSS_SELECTOR, 'a[href="/products"]').click()

# Tunggu dan ambil elemen produk (misalnya produk pertama)
product = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".product-overlay"))
)

# Scroll ke produk supaya overlay muncul
driver.execute_script("arguments[0].scrollIntoView();", product)

# Hover ke produk
ActionChains(driver).move_to_element(product).perform()

driver.find_element(By.CSS_SELECTOR, 'a[data-product-id="1"]').click()
driver.find_element(By.CSS_SELECTOR, "#cartModal > div > div > div.modal-footer > button").click()

print("Berhasil menambahkan ke keranjang bro!")

