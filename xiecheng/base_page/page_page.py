
from selenium import webdriver
from time import sleep

class BasePage():
    def __init__(self):
        self.driver = webdriver.Chrome('../../chromedriver.exe')
        self.driver.get("https://www.ctrip.com/")

        self.driver.maximize_window()
        sleep(1)

    def find_ele(self,*str):
        ele = self.driver.find_element(*str)
        return ele
