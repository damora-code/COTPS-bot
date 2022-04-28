import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
actions = ActionChains(driver)

number = '3054391830'
password = 'Guapotrader88!'

"""
Steps
0. Log in to COTPS --done
1. Go to Transaction page (refresh?) --done
2. Begin transaction --done
3. Sell
4. Confirm
5. Loop until you can't trade anymore (<$5)
6. Wait 2 hours to begin next cycle
"""

#step 0
driver.get('https://cotps.com/#/pages/login/login?originSource=userCenter')
time.sleep(5)
user_element = driver.find_element(by=By.XPATH, value="/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-input/div/input").send_keys(number)
password_element = driver.find_element(by=By.XPATH, value='/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-input/div/input').send_keys(password)
time.sleep(2)
login = driver.find_element(by=By.CLASS_NAME, value="login").click()

#step 1
time.sleep(10)
driver.get('https://cotps.com/#/pages/transaction/transaction')

#step 2
create_order = driver.find_element(by=By.XPATH, value='/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-button').click()
time.sleep(10)

#step 3 
#sell = driver.find_element_by_xpath
