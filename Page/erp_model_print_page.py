from base.findelment import Findelement

class erp_model_print_page():
    def __init__(self,driver):
        self.f=Findelement(driver)
    #获取完成按钮元素
    def get_shengchan_wangcheng(self):
        return self.f.get_element('shengchan_ok')
    #获取打印机元素
    def get_click_dayinji(self):
        return self.f.get_element('click_dayinji')
    #选择打印机元素
    def get_select_dayinji(self):
        return self.f.get_element('select_dayinji')
    #获取打印完成按钮
    def get_click_wancheng(self):
        return self.f.get_element('click_wancheng')
