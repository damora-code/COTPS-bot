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
driver.find_element(
    by=By.XPATH, value="//uni-view[5]/uni-input/div/input").send_keys(number)
driver.find_element(
    by=By.XPATH, value='//uni-view[7]/uni-input/div/input').send_keys(password)
time.sleep(2)
driver.find_element(by=By.CLASS_NAME, value="login").click()

time.sleep(2)
driver.get('https://cotps.com/#/pages/userCenter/myTeam')

time.sleep(5)
lv1 = driver.find_element(
    by=By.XPATH, value='//uni-view[1]/uni-view[2]/uni-view[2]')
lv1_bal = (lv1.get_attribute('innerHTML'))
print(lv1_bal)
