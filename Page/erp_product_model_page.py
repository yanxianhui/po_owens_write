from base.findelment import Findelement

class erp_product_model_page():
    def __init__(self,driver):
        self.f=Findelement(driver)

    #获取产品成型完成按钮元素
    def get_chengxing_wancheng(self):
        return self.f.get_element('chengxing_wancheng')
    #获取产品成型确认按钮元素
    def get_queding(self):
        return self.f.get_element('queding')
    