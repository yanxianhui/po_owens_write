from base.findelment import Findelement

class erp_product_baozhuang_page():
    def __init__(self,driver):
        self.f=Findelement(driver)

    #获取完成按钮元素
    def get_baozhuang_wangc_button(self):
        return self.f.get_element('baozhuang_wangc')
    #获取确认完成按钮
    def get_queren_ruku_button(self):
        return self.f.get_element('queren_ruku')