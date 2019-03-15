from base.findelment import Findelement

class erp_production_quality_page():
    def __init__(self,driver):
        self.f=Findelement(driver)

    #获取包装按钮元素
    def get_shengc_zhijian_button(self):
        return self.f.get_element('sc_zhijain_button')
    #获取包装质检按钮
    def get_baozhuangzhijian_button(self):
        return self.f.get_element('baozhuang_button')
    #获取质检确认按钮
    def get_zhijian_ok_button(self):
        return self.f.get_element('zhijian_ok')