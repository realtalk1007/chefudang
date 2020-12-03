from selenium_po.base import BasePage


class RepairrecordsPage(BasePage):


    _add_repair_records_button = ()
    # 添加按钮
    _car_owner_ele = ()
    # 车主姓名
    _deliver_ele = ()
    # 送修人
    _engine_num_ele = ()
    # 发动机号码
    _motorcycle_type_ele = ()
    # 车型
    _car_num_ele = ()
    # 车牌
    _small_car_type_ele = ()
    # 小车
    _big_bus_type_ele = ()
    # 大中客车
    _big_truck_type_ele = ()
    # 大型货车
    _other_car_type_ele = ()
    # 其他
    _vin_ele = ()
    # vin码
    _vehicle_maintenance_ele = ()
    # 汽车维护
    _trouble_repair_ele = ()
    # 故障维修
    _accident_repair_ele = ()
    # 事故维修
    _sendrepair_date_ele = ()
    # 送修时间
    _setdate_ele = ()
    # 结算时间
    _wugenghuan_ele = ()
    # 无更换配件
    _tuoxiufang_ele = ()
    # 托修方收回
    _chengxiufang_ele = ()
    # 承修方收回
    _fault_description = ()
    # 故障描述
    _fault_reason = ()
    # 故障原因
    _XiaoXiu_ele = ()
    # 小修
    _ZongCheng_ele = ()
    # 总成
    _ZhengChe_ele = ()
    # 整车
    _YiWei_ele = ()
    # 一维
    _ErWei_ele = ()
    # 二维
    _start_miles = ()
    # 送修里程数
    _end_miles = ()
    # 出厂里程数
    _owner_phone_num = ()
    # 车主号码
    _settlement_clerk = ()
    # 结算员
    _repair_records_save_button = ()
    # 保存按钮

    # 点击添加按钮
    def go_to_add_repair_records(self):
        self.find_and_click(self._add_repair_records_button)
        return self


    # 填写车主姓名
    def add_car_owner(self, car_owner):
        self.find_and_sendkeys(self._car_owner_ele, car_owner)
        return self

    # 填写送修人姓名
    def add_deliver(self, deliver):
        self.find_and_sendkeys(self._deliver_ele, deliver)
        return self

    # 填写发动机号码
    def add_engine_num(self, engine_num):
        self.find_and_sendkeys(self._engine_num_ele, engine_num)
        return self

    # 填写车型
    def add_motorcycle_type(self, motorcycle_type):
        self.find_and_sendkeys(self._motorcycle_type_ele, motorcycle_type)
        return self

    # 填写车牌
    def add_car_num(self, car_num):
        self.find_and_sendkeys(self._car_num_ele, car_num)
        return self

    # 选择车型
    def add_vehicle_type(self, vehicle_type):
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
    def add_vin(self, vin):
        self.find_and_sendkeys(self._vin_ele, vin)
        return self

    # 添加维修企业名称(信息自带)
    def add_enterprise_name(self):
        pass

    # 添加维修企业地址(信息自带)
    def add_enterprise_address(self):
        pass

    # 选择维修性质
    def choose_repair_nature(self, repair_nature):
        if repair_nature == '汽车维护':
            self.find_and_click(self._vehicle_maintenance_ele)
        elif repair_nature == '故障修理':
            self.find_and_click(self._trouble_repair_ele)
        else:
            self.find_and_click(self._accident_repair_ele)
        return self

    # 选择送修时间  格式 2020-12-03
    def add_sendrepair_date(self, sendrepair_date):
        js = "document.getElementById('sendrepairdate').removeAttribute('readonly')"
        self._driver.execute_script(js)
        self.find_and_sendkeys(self._sendrepair_date_ele, sendrepair_date)
        return self

        # 选择结算时间

    def add_setdate(self, setdate):
        js = "document.getElementById('setdate').removeAttribute('readonly')"
        self._driver.execute_script(js)
        self.find_and_sendkeys(self._setdate_ele, setdate)
        return self

    # 选择旧件处理结果
    def choose_way_junk_handle(self, handle_result):
        if handle_result == '无更换配件':
            self.find_and_click(self._wugenghuan_ele)
        elif handle_result == '旧件已确认，由托修方收回':
            self.find_and_click(self._tuoxiufang_ele)
        else:
            self.find_and_click(self._chengxiufang_ele)
        return self

    # 故障描述
    def add_fault_description(self, fault_description):
        self.find_and_sendkeys(self._fault_description, fault_description)
        return self

    # 故障原因
    def add_fault_reason(self, fault_reason):
        self.find_and_sendkeys(self._fault_reason, fault_reason)
        return self

    # 选择维修类别
    def choose_repair_category(self, repair_category):
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
    def add_start_miles(self, start_miles):
        self.find_and_sendkeys(self._start_miles, start_miles)
        return self

    # 添加出厂里程
    def add_end_miles(self, end_miles):
        self.find_and_sendkeys(self._end_miles, end_miles)
        return self

    # 车主联系电话
    def add_owner_phone_num(self, owner_phone_num):
        self.find_and_sendkeys(self._owner_phone_num, owner_phone_num)
        pass

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

    # 添加结算员(信息自带)
    def add_settlement_clerk(self, settlement_clerk):
        self.find_and_sendkeys(self._settlement_clerk, settlement_clerk)

    # 点击保存按钮
    def click_save_button(self):
        self.find_and_click(self._repair_records_save_button)
        return self
