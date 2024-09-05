from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

cesta = "chromedriver-win64\\chromedriver.exe"

x = 301

s = Service(executable_path=cesta)
ooptions = webdriver.ChromeOptions()
ooptions.headless = False
driver = webdriver.Chrome(service=s, options=ooptions)

driver.get('link')

var = 1

while var == 1:
    time.sleep(10)
    elem = driver.find_element(By.XPATH, "full xpath")
    elem.click()
    for i in range(x):
        print(i)
        time.sleep(1)

    driver.refresh()

input('Stiskni enter pro konec')

