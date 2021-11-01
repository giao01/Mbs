
from selenium.webdriver.common.by import By
from gao5.xiecheng.base_page.page_page import *

class BaiduPage(BasePage):
    get_input = (By.ID,'kw')
    get_bater = (By.ID,'su')

    def get_ele_input(self):
        ele = self.find_ele(*BaiduPage.get_input)
        return ele

    def get_ele_bater(self):
        ele = self.find_ele(*BaiduPage.get_bater)
        return ele

    def sousu(self,str):
        self.get_ele_input().send_keys(str)
        self.get_ele_bater().click()