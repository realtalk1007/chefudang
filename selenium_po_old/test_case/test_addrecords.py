import pytest
import yaml

from selenium_po_old.page.loginpage import LoginPage

def get_records_add_datas():
    with open('../records_add.yaml', 'r', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        return datas

class TestWeixin:
    def setup(self):
        self.login = LoginPage()

    def teardown(self):
        self.login.close()

    @pytest.mark.parametrize(
        'username,password,car_owner,deliver,engine_num,motorcycle_type,car_num,vehicle_type,vin,\
        repair_nature,senddate,setdate,handle_result,fault_description,fault_reason,\
        repair_category,start_miles,end_miles,owner_phone_num,settclerk',get_records_add_datas()
    )
    def test_add_repair_records(self,username,password,car_owner,deliver,engine_num,motorcycle_type,car_num,
                        vehicle_type,vin,repair_nature,senddate,setdate,handle_result,
                        fault_description,fault_reason,repair_category,start_miles,end_miles,owner_phone_num,settclerk):
        result = self.login.add_username(username).add_password(password).click_login().go_to_repair_collection().go_to_add_repair_records().\
            add_car_owner(car_owner).add_deliver(deliver).add_engine_num(engine_num).add_motorcycle_type(motorcycle_type).\
            add_car_num(car_num).add_vehicle_type(vehicle_type).add_vin(vin).choose_repair_nature(repair_nature).\
            add_sendrepair_date(senddate).add_setdate(setdate).choose_way_junk_handle(handle_result).add_fault_description(fault_description).\
            add_fault_reason(fault_reason).choose_repair_category(repair_category).add_start_miles(start_miles).add_end_miles(end_miles).\
            add_owner_phone_num(owner_phone_num).add_settlement_clerk(settclerk).click_save_button().click_repair_records_refresh().get_car_num_list()
        print(result)
        print(car_owner)
        assert car_num not in result