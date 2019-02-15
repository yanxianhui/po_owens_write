from base.findelment import Findelement

class erp_design_quality_page():
    def __init__(self,driver):
        self.f=Findelement(driver)

    #获取设计质检界面指派订单元素
    def get_d_zj_zhipaidingdan_button(self):
        return self.f.get_element('sheji_zhipai')

    #获取指派订单确认按钮
    def get_d_zj_zhipai_quren_button(self):
        return self.f.get_element('sheji_zhipaiqueren')

    #获取审核通过按钮元素
    def get_d_zj_shehetongguo_button(self):
        return self.f.get_element('sheji_shehe')