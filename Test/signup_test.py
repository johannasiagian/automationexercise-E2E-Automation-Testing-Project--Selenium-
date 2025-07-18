from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/login")
driver.maximize_window()

#Step 1 
driver.find_element(By.CSS_SELECTOR, '[data-qa="signup-name"]').send_keys("Andika")
driver.find_element(By.CSS_SELECTOR, '[data-qa="signup-email"]').send_keys("andikawowsekali123@gmail.com")
driver.find_element(By.CSS_SELECTOR, '[data-qa="signup-button"]').click()

time.sleep(5)
print("Berhasil register")

#Step 2 - Fill Information  Account Information
driver.find_element(By.ID, "id_gender1").click()
driver.find_element(By.ID, "password").send_keys("andikawowsekali123")
dropdown = Select(driver.find_element(By.ID, "days"))
dropdown.select_by_value("9")
dropdown = Select(driver.find_element(By.ID, "months"))
dropdown.select_by_value("5")
dropdown = Select(driver.find_element(By.ID, "years"))
dropdown.select_by_value("2000")
driver.find_element(By.CSS_SELECTOR, "#newsletter").click()
driver.find_element(By.CSS_SELECTOR, "#optin").click()

#Step 3 - Fill Information Address Information
driver.find_element(By.ID, "first_name").send_keys("Putra")
driver.find_element(By.ID, "last_name").send_keys("Abimana")
driver.find_element(By.ID, "company").send_keys("PutraJaya")
driver.find_element(By.ID, "address1").send_keys("Jl.Kebangsaan")
driver.find_element(By.ID, "address2").send_keys("-")
dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_value("Singapore")
driver.find_element(By.ID, "state").send_keys("Singapore")
driver.find_element(By.ID, "city").send_keys("Jurong")
driver.find_element(By.ID, "zipcode").send_keys("588193")
driver.find_element(By.ID, "mobile_number").send_keys("0812345678")
driver.find_element(By.CSS_SELECTOR, "#form > div > div > div > div.login-form > form > button").click()


print("Berhasil Membuat Akun")

driver.quit()


                                      