from ast import Continue
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.execute_script("document.body.style.zoom='50%'")
actions = ActionChains(driver)
number = '3054391830'
password = 'Guapotrader88!'

#step 0
driver.get('https://cotps.com/#/pages/login/login?originSource=userCenter')
time.sleep(5)
user_element = driver.find_element(by=By.XPATH, value="//uni-view[5]/uni-input/div/input").send_keys(number)
password_element = driver.find_element(by=By.XPATH, value='//uni-view[7]/uni-input/div/input').send_keys(password)
time.sleep(2)
login = driver.find_element(by=By.CLASS_NAME, value="login").click()

#step 1
time.sleep(5)
driver.get('https://cotps.com/#/pages/transaction/transaction')

#step 2
time.sleep(6)
while True:
    create_order = driver.find_element(By.CLASS_NAME, 'orderBtn').click()
    time.sleep(10)
    #step 3
    sell = driver.find_element(by=By.XPATH, value='//uni-button[2]').click()
    time.sleep(10)
    #step 4
    confirm = driver.find_element(by=By.XPATH, value='//uni-view[8]/uni-view/uni-button').click()
    time.sleep(10)
    # try:
    #     txn_e = driver.find_elements(by=By.CLASS_NAME, value='uni-toast')
    # except NoSuchElementException:
    #     print("No element found")
    # else:
    #     print("Below $5.. Please wait")
    #     time.sleep(10)
    # if txn_e is True:
    #     WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-view/uni-view/uni-view[6]/uni-button[2]")))
    #     #sell = driver.find_element(by=By.XPATH, value='/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-view/uni-view/uni-view[6]/uni-button[2]').click()
    #     time.sleep(10)
    #     WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[8]/uni-view/uni-view/uni-button")))
    #     #confirm = driver.find_element(by=By.XPATH, value='/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[8]/uni-view/uni-view/uni-button').click()
    #     time.sleep(10)
