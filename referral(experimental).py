from ast import Continue
import time
from xml.dom import ValidationErr
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

while True:
    time.sleep(5)
    lv1 = driver.find_element(
        by=By.XPATH, value='//uni-view[1]/uni-view[2]/uni-view[2]')
    lv1_bal = (float(lv1.get_attribute('innerHTML')))
    print("lv1 balance: ", lv1_bal)
    if lv1_bal == 0:
        print("Balance less than 0 for Lv1, continuing to Lv2")
        driver.find_element(
            By.XPATH, value='//uni-view/uni-view[1]/uni-view[2]').click()
        time.sleep(5)

        lv2 = driver.find_element(
            By.XPATH, value='//uni-view[1]/uni-view[2]/uni-view[2]')
        lv2_bal = (float(lv2.get_attribute('innerHTML')))
        print("lv2 balance: ", lv2_bal)

        if lv2_bal == 0:
            print("Balance less than 0 for Lv2, continuing to Lv3")
            driver.find_element(
                By.XPATH, value='//uni-view/uni-view[1]/uni-view[3]').click()
            time.sleep(5)
        lv3 = driver.find_element(
            By.XPATH, value='//uni-view[1]/uni-view[2]/uni-view[2]')
        lv3_bal = (float(lv3.get_attribute('innerHTML')))
        print("lv3 balance: ",lv3_bal)

        if lv3_bal == 0:
            print("Balance less than 0 for Lv3, waiting for next cycle..")
            timer()
            driver.get('https://cotps.com/#/pages/userCenter/myTeam')

    elif lv1_bal > 0:
        print("Greater than 0, collecting residual income")
        receive = driver.find_element(
            By.XPATH, value='//uni-view/uni-view[2]/uni-view/uni-button').click()
        time.sleep(5)

        lv2 = driver.find_element(
            By.XPATH, value='//uni-view[1]/uni-view[2]/uni-view[2]')
        lv2_bal = (float(lv2.get_attribute('innerHTML')))
        print(lv2_bal)
        if lv2_bal > 0:
            print("Greater than 0, collecting residual income")
        receive = driver.find_element(
            By.XPATH, value='//uni-view/uni-view[2]/uni-view/uni-button').click()
        time.sleep(5)
        if lv3_bal > 0:
            print("Greater than 0, collecting residual income")
        receive = driver.find_element(
            By.XPATH, value='//uni-view/uni-view[2]/uni-view/uni-button').click()
        print("Waiting for next cycle...")
        timer()
        driver.get('https://cotps.com/#/pages/userCenter/myTeam')
