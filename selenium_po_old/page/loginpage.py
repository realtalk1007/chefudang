from selenium.webdriver.common.by import By

from selenium_po_old.base import BasePage
from selenium_po_old.page.repairrecordspage import RepairrecordsPage


class LoginPage(BasePage):
    _username = (By.XPATH,'//*[@id="oper_code"]')
    _password = (By.XPATH,'//*[@id="password"]')
    _base_url = 'http://jx.chefudang.cn/repair-station/login/login.htm'
    # _password = (By.ID,'password')
    _login = (By.ID,'btn_dologin')
    def add_username(self,username):
        self.find_and_sendkeys(self._username,username)
        return self

    def add_password(self,password):
        self.find_and_sendkeys(self._password,password)
        return self

    def click_login(self):
        self.find_and_click(self._login)
        return RepairrecordsPage(self._driver)