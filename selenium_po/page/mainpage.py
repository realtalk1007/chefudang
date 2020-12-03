from selenium.webdriver.common.by import By

from selenium_po.base import BasePage


class MainPage(BasePage):

    _add_repair_reocrds = (By.CSS_SELECTOR,"#tab-317 > span > i")
    def go_to_add_repair_records(self):
        self.find_and_click(self._add_repair_reocrds)
        return




