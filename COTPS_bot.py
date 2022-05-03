import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from decouple import config

driver = webdriver.Chrome()
driver.maximize_window()
actions = ActionChains(driver)
number = config('NUMBER')
password = config('PASSWORD')

# step 0
driver.get('https://cotps.com/#/pages/login/login?originSource=userCenter')
time.sleep(5)
user_element = driver.find_element(
    by=By.XPATH, value="//uni-view[5]/uni-input/div/input").send_keys(number)
password_element = driver.find_element(
    by=By.XPATH, value='//uni-view[7]/uni-input/div/input').send_keys(password)
time.sleep(2)
login = driver.find_element(by=By.CLASS_NAME, value="login").click()

# step 1
time.sleep(5)
driver.get('https://cotps.com/#/pages/transaction/transaction')
time.sleep(5)
bal = driver.find_element(By.XPATH, '//uni-view[3]/uni-view[2]/uni-view[2]')
balance = (float(bal.get_attribute('innerHTML')))
print(type(balance))
if balance < 4.4:
    print("less than 4.4")
else:
    print("greater than 4.4")

# step 2
# while True:
#     create_order = driver.find_element(By.CLASS_NAME, 'orderBtn').click()
#     time.sleep(10)
#     #step 3
#     sell = driver.find_element(by=By.XPATH, value='//uni-button[2]').click()
#     time.sleep(10)
#     #step 4
#     confirm = driver.find_element(by=By.XPATH, value='//uni-view[8]/uni-view/uni-button').click()
#     time.sleep(10)
