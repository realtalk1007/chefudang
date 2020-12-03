from selenium.webdriver.common.by import By

from selenium_po.base import BasePage
from selenium_po.page.mainpage import MainPage


class LoginPage(BasePage):
    _username = (By.LINK_TEXT,'请输入用户名')
    _password = (By.LINK_TEXT,'请输入密码')
    _login = (By.LINK_TEXT,'登 录')
    def add_username(self,username):
        self.find_and_sendkeys(self._username,username)
        return self

    def add_password(self,password):
        self.find_and_sendkeys(self._password,password)
        return self

    def click_login(self):
        self.find_and_click(self._login)

        return MainPage(self._driver)