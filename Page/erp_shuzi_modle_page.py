from base.findelment import Findelement

class erp_shuzi_modle_page():
    def __init__(self,driver):
        self.f=Findelement(driver)

    #获取数字建模界面指派订单元素
    def get_sz_zhipaidingdan_button(self):
        return self.f.get_element('s_zhipai')

    #获取指派订单确认按钮
    def get_sz_zhipai_quren_button(self):
        return self.f.get_element('s_zhipaiqueren')

    #获取审核通过按钮元素
    def get_sz_shehetongguo_button(self):
        return self.f.get_element('s_shenhe')