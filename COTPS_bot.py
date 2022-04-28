import time
from selenium import webdriver, ActionChains

driver = webdriver.Chrome()

#Test to sure that driver is correctly added
"""
driver.get('http://www.google.com')
time.sleep(5)
search_box = driver.find_element_by_name('q')
search_box.send_keys('USDT Price')
search_box.submit()
time.sleep(5)
"""

"""
Steps
0. Log in to COTPS (Automate first then come back to this)
1. Go to Transaction page (refresh?)
2. Begin transaction
3. Sell
4. Confirm
5. Loop until you can't trade anymore (<$5)
6. Wait 2 hours to begin next cycle
"""

driver.get('https://www.cotps.com/#/pages/transaction/transaction')
create_order = driver.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-button')
create_order.click()
time.sleep(10)
sell = driver.find_element_by_xpath
