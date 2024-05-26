from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options=Options()
service=Service()


class BookStore:
    def __init__(self):
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    def navigating_store(self):
        self.driver.get("https://automationbookstore.dev/")

    def calculate_books(self):
        count=self.driver.find_elements(By.XPATH,value="//li/a/img[@class='ui-li-thumb']")
        return len(count)

def validation():
    bookst=BookStore()
    bookst.navigating_store()
    try:
        assert bookst.calculate_books() == 7
        print("Test Case Executed Successfully")

    except:
        print("Test Case Failed")



validation()

