from ast import Continue
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
actions = ActionChains(driver)

number = '3054391830'
password = 'Guapotrader88!'

#step 0
driver.get('https://cotps.com/#/pages/login/login?originSource=userCenter')
time.sleep(5)
user_element = driver.find_element(by=By.XPATH, value="/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-input/div/input").send_keys(number)
password_element = driver.find_element(by=By.XPATH, value='/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-input/div/input').send_keys(password)
time.sleep(2)
login = driver.find_element(by=By.CLASS_NAME, value="login").click()

#step 1
time.sleep(5)
driver.get('https://cotps.com/#/pages/transaction/transaction')

#step 2
time.sleep(5)
while True:
    create_order = driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-button').click()
    try:
        txn_e = driver.find_elements(by=By.CLASS_NAME, value='uni-toast')
    except NoSuchElementException:
        print("No element found")
    if txn_e is True:
        sell = driver.find_element(by=By.XPATH, value='/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-view/uni-view/uni-view[6]/uni-button[2]').click()
        time.sleep(10)
        confirm = driver.find_element(by=By.XPATH, value='/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[8]/uni-view/uni-view/uni-button').click()
        time.sleep(10)
    else:
        print("Below $5.. Please wait")
        time.sleep(5)
# #step 3 
   # sell = driver.find_element(by=By.XPATH, value='/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-view/uni-view/uni-view[6]/uni-button[2]').click()
# time.sleep(10)

# #step 4
  #  confirm = driver.find_element(by=By.XPATH, value='/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[8]/uni-view/uni-view/uni-button').click()

