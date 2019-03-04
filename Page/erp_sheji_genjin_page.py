from base.findelment import Findelement

class erp_sheji_genjin_page():
    def __init__(self,driver):
        self.f=Findelement(driver)

    #获取设计跟进界面指派订单元素
    def get_shejigenjin_fenpei_button(self):
        return self.f.get_element('fenpei_button')

    #获取设计跟进界面分配确认按钮元素
    def get_shejigenjin_fenpei_queren_button(self):
        return self.f.get_element('fenpei_queren')

    #获取设计跟进界面处方button
    def get_shejigenjin_chufang_button(self):
        return self.f.get_element('chufang_button')



