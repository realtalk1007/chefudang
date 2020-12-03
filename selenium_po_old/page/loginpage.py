from selenium.webdriver.common.by import By

from selenium_po.base import BasePage
from selenium_po.page.mainpage import MainPage


class LoginPage(BasePage):
    _username = (By.CSS_SELECTOR,".input_login:nth-child(0)")
    _password = (By.XPATH,'//*[@id="password"]')
    # _password = (By.ID,'password')
    _login = (By.ID,'btn_login')
    def add_username(self,username):
        self.find_and_sendkeys(self._username,username)
        return self

    def add_password(self,password):
        self.find_and_sendkeys(self._password,password)
        return self

    def click_login(self):
        self.find_and_click(self._login)

        return MainPage(self._driver)