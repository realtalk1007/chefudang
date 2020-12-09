from selenium.webdriver.common.by import By
import time
from selenium_po.base import BasePage

class RepairrecordsPage(BasePage):
    _iframe_left_menu = (By.ID,'left_menu')
    # 左菜单iframe元素
    _iframe_weixiujilu = (By.XPATH,'//*[@id="nav-tabs"]/div[2]/div[2]/div/iframe')
    # 维修记录页面iframe
    _iframe_xinzengweixiujilu = (By.XPATH,'//*[@id="nav-tabs"]/div[2]/div[3]/div/iframe')
    # 新增维修记录页面iframe
    _repair_collection_ele = (By.XPATH,'//*[@id="100000001232"]/li[1]/div/span[3]')
    _add_repair_records_ele = (By.XPATH,'/html/body/div[2]/div[1]/div[2]/div/div/div[1]/table/tbody/tr/td[3]/a/span/span')
    _car_owner_ele = (By.XPATH,'//*[@id="caruser"]')
    _deliver_ele = (By.XPATH,'//*[@id="linkman"]')
    _engine_num_ele = (By.ID,"enginenumber")
    _motorcycle_type_ele = (By.ID,'carmodel')
    _car_num_ele = (By.ID,'carno')
    _vehicle_type_arrow = (By.XPATH,'//*[@id="myForm"]/table/tbody/tr[3]/td[4]/span/span/span')
    # 车型菜单箭头
    _small_car_type_ele = (By.XPATH,'/html/body/div[5]/div/div[1]')
    _big_bus_type_ele = (By.XPATH,'/html/body/div[5]/div/div[2]')
    _big_truck_type_ele = (By.XPATH,'/html/body/div[5]/div/div[3]')
    _other_car_type_ele = (By.XPATH,'/html/body/div[5]/div/div[3]')
    _vin_ele = (By.ID,'carvin')
    _repair_nature_arrow = (By.XPATH,'//*[@id="myForm"]/table/tbody/tr[6]/td[2]/span/span/span')
    # 维修性质菜单箭头
    _vehicle_maintenance_ele = (By.XPATH,'/html/body/div[6]/div/div[1]')
    _trouble_repair_ele = (By.XPATH,'/html/body/div[6]/div/div[2]')
    _accident_repair_ele = (By.XPATH,'/html/body/div[6]/div/div[3]')
    # 送修时间iframe
    _sendrepair_date_ele = (By.ID,'sendrepairdate')
    # 结算时间iframe
    _setdate_ele = (By.ID,'setdate')
    _junk_handle_arrow = (By.XPATH,'//*[@id="myForm"]/table/tbody/tr[9]/td[2]/span/span/span')
    # 旧件处理下拉菜单
    _wugenghuan_ele = (By.XPATH,'/html/body/div[8]/div/div[1]')
    _tuoxiufang_ele = (By.XPATH,'/html/body/div[8]/div/div[2]')
    _chengxiufang_ele = (By.XPATH,'/html/body/div[8]/div/div[3]')
    _fault_description = (By.ID,'faultdescript')
    _fault_reason = (By.ID,'faultreason')
    _repair_category_arrow = (By.XPATH,'//*[@id="myForm"]/table/tbody/tr[6]/td[4]/span/span/span')
    _XiaoXiu_ele = (By.XPATH,'/html/body/div[7]/div/div[1]')
    _ZongCheng_ele = (By.XPATH,'/html/body/div[7]/div/div[2]')
    _ZhengChe_ele = (By.XPATH,'/html/body/div[7]/div/div[3]')
    _YiWei_ele = (By.XPATH,'/html/body/div[7]/div/div[4]')
    _ErWei_ele = (By.XPATH,'/html/body/div[7]/div/div[5]')
    _start_miles =(By.ID,'repairmile')
    _end_miles = (By.ID,'leavemile')
    _owner_phone_num = (By.ID,'mobilephone')
    _settclerk = (By.ID,'settclerk')
    _repair_records_save_button =(By.XPATH,'//*[@id="add_btn_save"]/span/span')
    _repair_records_refresh_ele = (By.XPATH,'/html/body/div[2]/div[1]/div[2]/div/div/div[1]/table/tbody/tr/td[1]/a/span/span')
    _car_num_list_ele = (By.XPATH,'/html/body/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/table')

    def go_to_repair_collection(self):
        self._driver.switch_to.frame(self.find(self._iframe_left_menu))
        # self._driver.switch_to.frame(self.find_and_click(self._repair_collection_ele))
        self.find_and_click(self._repair_collection_ele)
        self._driver.switch_to.default_content()
        return self

    # 点击添加按钮
    def go_to_add_repair_records(self):
        self._driver.switch_to.frame(self.find(self._iframe_weixiujilu))
        self.find_and_click(self._add_repair_records_ele)
        self._driver.switch_to.default_content()
        return self

    # 填写车主姓名
    def add_car_owner(self,car_owner):
        self._driver.switch_to.frame(self.find(self._iframe_xinzengweixiujilu))
        self.find_and_sendkeys(self._car_owner_ele,car_owner)
        return self

    # 填写送修人姓名
    def add_deliver(self,deliver):
        self.find_and_sendkeys(self._deliver_ele,deliver)
        return self

    # 填写发动机号码
    def add_engine_num(self,engine_num):
        self.find_and_sendkeys(self._engine_num_ele,engine_num)
        return self

    # 填写车型
    def add_motorcycle_type(self,motorcycle_type):
        self.find_and_sendkeys(self._motorcycle_type_ele,motorcycle_type)
        return self

    # 填写车牌
    def add_car_num(self,car_num):
        self.find_and_sendkeys(self._car_num_ele,car_num)
        return self

    # 选择车型
    def add_vehicle_type(self,vehicle_type):
        self.find_and_click(self._vehicle_type_arrow)

        if vehicle_type == '小型车':
            self.find_and_click(self._small_car_type_ele)
        elif vehicle_type == '大中型客车':
            self.find_and_click(self._big_bus_type_ele)
        elif vehicle_type == '大型货车':
            self.find_and_click(self._big_truck_type_ele)
        else:
            self.find_and_click(self._other_car_type_ele)
        return self

    # 填加vin
    def add_vin(self,vin):
        self.find_and_sendkeys(self._vin_ele,vin)
        return self

    # 添加维修企业名称(信息自带)
    def add_enterprise_name(self):
        pass

    # 添加维修企业地址(信息自带)
    def add_enterprise_address(self):
        pass

    # 选择维修性质
    def choose_repair_nature(self,repair_nature):
        self.find_and_click(self._repair_nature_arrow)
        if repair_nature == '汽车维护':
            self.find_and_click(self._vehicle_maintenance_ele)
        elif repair_nature == '故障修理':
            self.find_and_click(self._trouble_repair_ele)
        else:
            self.find_and_click(self._accident_repair_ele)
        return self


    # 选择送修时间  格式 2020-12-03
    def add_sendrepair_date(self,senddate):
        js = "document.getElementById('sendrepairdate').removeAttribute('readonly')"
        self._driver.execute_script(js)
        # time.sleep(10)
        self.find_and_sendkeys(self._sendrepair_date_ele,senddate)
        return self

        # 选择结算时间
    def add_setdate(self,setdate):
        js = "document.getElementById('setdate').removeAttribute('readonly')"
        self._driver.execute_script(js)
        self.find_and_sendkeys(self._setdate_ele, setdate)
        return self

    # 选择旧件处理结果
    def choose_way_junk_handle(self,handle_result):
        self.find_and_click(self._junk_handle_arrow)
        if handle_result == '无更换配件':
            self.find_and_click(self._wugenghuan_ele)
        elif handle_result == '旧件已确认，由托修方收回':
            self.find_and_click(self._tuoxiufang_ele)
        else:
            self.find_and_click(self._chengxiufang_ele)
        return self

    # 故障描述
    def add_fault_description(self,fault_description):
        self.find_and_sendkeys(self._fault_description,fault_description)
        return self

    # 故障原因
    def add_fault_reason(self,fault_reason):
        self.find_and_sendkeys(self._fault_reason, fault_reason)
        return self

    # 选择维修类别
    def choose_repair_category(self,repair_category):
        self.find_and_click(self._repair_category_arrow)
        if repair_category == '小修':
            self.find_and_click(self._XiaoXiu_ele)
        elif repair_category == '总成':
            self.find_and_click(self._ZongCheng_ele)
        elif repair_category == '整车':
            self.find_and_click(self._ZhengChe_ele)
        elif repair_category == '一维':
            self.find_and_click(self._YiWei_ele)
        else:
            self.find_and_click(self._ErWei_ele)
        return self

    # 添加送修里程
    def add_start_miles(self,start_miles):
        self.find_and_sendkeys(self._start_miles,start_miles)
        return self

    # 添加出厂里程
    def add_end_miles(self,end_miles):
        self.find_and_sendkeys(self._end_miles,end_miles)
        return self

    # 车主联系电话
    def add_owner_phone_num(self,owner_phone_num):
        self.find_and_sendkeys(self._owner_phone_num,owner_phone_num)
        return self

    # 企业联系人(信息自带)
    def add_contact_name(self):
        pass

    # 添加联系人电话(信息自带)
    def add_contact_phone_num(self):
        pass

    # 添加工单号(信息自带)
    def add_dispatch_num(self):
        pass

    # 添加结算清单编号(信息自带)
    def settlement_list_num(self):
        pass

    # 添加结算员
    def add_settlement_clerk(self,settclerk):
        self.find_and_sendkeys(self._settclerk,settclerk)
        return self

    # 点击保存按钮
    def click_save_button(self):
        self.find_and_click(self._repair_records_save_button)
        self._driver.switch_to.default_content()
        return self
    # 点击刷新按钮
    def click_repair_records_refresh(self):
        self._driver.switch_to.frame(self.find(self._iframe_weixiujilu))
        self.find_and_click(self._repair_records_refresh_ele)
        return self

    def get_car_num_list(self):
        car_num_list = self.finds(self._car_num_list_ele)
        # time.sleep(5)
        list0 = []
        for carno in car_num_list:
            # new_carno = carno.replace('\n', '')
            # new_carno = carno.strip("")
            list0.append(carno.text)

        # priceList = ['\n\t\t\t\t\t\t\t\tCHF\xa0\r\n        \r\n    \t64.90',
        #              '\n\t\t\t\t\t\t\t\tCHF\xa0\r\n        \r\n    \t58.40',
        #              '\n\t\t\t\t\t\t\t\tCHF\xa0\r\n        \r\n    \t48.70']
        #
        # print([' '.join([i.strip() for i in price.strip().split('\t')]) for price in priceList])
        list1 = [' '.join([i.strip() for i in price.strip().split('\n')]) for price in list0]
        return list1



