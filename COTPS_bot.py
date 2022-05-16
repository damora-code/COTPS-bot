import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import config
from timer import timer
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
country_code = config('COUNTRY')
number = config('NUMBER')
password = config('PASSWORD')

driver.get('https://cotps.com/#/pages/login/login?originSource=userCenter')
country = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, "//uni-view/uni-view[5]/uni-text"))).click()
country_insert = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, "//uni-view/uni-input/div/input"))).send_keys(country_code)
go_back = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//uni-view/uni-view[1]/uni-button"))).click()
username = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, "//uni-view[5]/uni-input/div/input"))).send_keys(number)
password_ = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, "//uni-view[7]/uni-input/div/input"))).send_keys(password)
login = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "login"))).click()
time.sleep(7)
driver.get('https://cotps.com/#/pages/transaction/transaction')

while True:
    bal = driver.find_element(
        By.XPATH, '//uni-view[3]/uni-view[2]/uni-view[2]')
    balance = (float(bal.get_attribute('innerHTML')))
    print("Balance: ", balance)
    if balance < 5:
        print("Balance less than $5 please wait")
        timer()
        driver.get('https://cotps.com/#/pages/transaction/transaction')
    else:
        print("Greater than $5, beginning transactions")
        create_order = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "orderBtn"))).click()
        sell_order = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//uni-button[2]"))).click()
        confirm_order = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//uni-view[8]/uni-view/uni-view/uni-button"))).click()