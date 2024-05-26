import time

import options
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options=Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://www.google.com/")
time.sleep(5)
driver.find_element(By.XPATH,value="//textarea[@id='APjFqb']").send_keys("Python")
time.sleep(5)
print(driver.title)













