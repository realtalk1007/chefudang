from selenium_po.base import BasePage
from selenium_po.page.repairrecordspage import RepairrecordsPage


class DataCollection(BasePage):
    _rapair_data_button = ''
    _repair_records_button = ''
    def go_to_repair_data(self):
        self.find_and_click(self._rapair_data_button)
        return self

    def go_to_repair_records(self):
        self.find_and_click(self._repair_records_button)
        return RepairrecordsPage(self._driver)

