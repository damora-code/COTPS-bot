import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import config
from timer import timer

driver = webdriver.Chrome()
driver.maximize_window()
number = config('NUMBER')
password = config('PASSWORD')

driver.get('https://cotps.com/#/pages/login/login?originSource=userCenter')
time.sleep(5)
user_element = driver.find_element(
    by=By.XPATH, value="//uni-view[5]/uni-input/div/input").send_keys(number)
password_element = driver.find_element(
    by=By.XPATH, value='//uni-view[7]/uni-input/div/input').send_keys(password)
time.sleep(2)
login = driver.find_element(by=By.CLASS_NAME, value="login").click()

time.sleep(5)
driver.get('https://cotps.com/#/pages/transaction/transaction')

while True:
    time.sleep(5)
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
        create_order = driver.find_element(By.CLASS_NAME, 'orderBtn').click()
        time.sleep(10)
        # step 3
        sell = driver.find_element(
            by=By.XPATH, value='//uni-button[2]').click()
        time.sleep(10)
        # step 4
        confirm = driver.find_element(
            by=By.XPATH, value='//uni-view[8]/uni-view/uni-view/uni-button').click()
        time.sleep(10)
