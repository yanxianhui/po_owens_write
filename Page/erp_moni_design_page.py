from base.findelment import Findelement

class erp_moni_design_page():
    def __init__(self,driver):
        self.f=Findelement(driver)

    #获取模拟排牙界面指派订单元素
    def get_moni_zhipaidingdan_button(self):
        return self.f.get_element('m_zhipai')

    #获取指派订单确认按钮
    def get_moni_zhipai_quren_button(self):
        return self.f.get_element('m_zhipaiqueren')

    #获取审核通过按钮元素
    def get_moni_shehetongguo_button(self):
        return self.f.get_element('m_shehe')