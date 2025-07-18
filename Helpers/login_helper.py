import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/signup")

def do_login(driver,email,password):
    driver.find_element(By.CSS_SELECTOR, "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > input[type=email]:nth-child(2)").send_keys("andikawowsekali123@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > input[type=password]:nth-child(3)").send_keys("andikawowsekali123")
    driver.find_element(By.CSS_SELECTOR, "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > button").click()
    print("Berhasil login ea")
    