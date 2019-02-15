from base.findelment import Findelement

class erp_product_schedu_page():
    def __init__(self,driver):
        self.f=Findelement(driver)

    #获取选择框元素
    def get_xuanze_kuan(self):
        return self.f.get_element('xuanze_kuan')
    #获取排产预览按钮元素
    def get_paican_yulan(self):
        return self.f.get_element('paican_yulan')
    #获取流转号输入文本框
    def get_liuzhuanghao(self):
        return self.f.get_element('liuzhuanghao')
    #获取确认排产确认按钮元素
    def get_queren_paichang(self):
        return self.f.get_element('queren_paichang')