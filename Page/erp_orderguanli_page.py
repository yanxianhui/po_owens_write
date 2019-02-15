from base.findelment import Findelement

class erp_orderguanli_page():
    def __init__(self,driver):
        self.f=Findelement(driver)

    # 获取设计按钮元素
    def get_sheji_button(self):
        return self.f.get_element('sheji_button')
    #获取创建订单按钮元素
    def get_chaungjian_order_button(self):
        return self.f.get_element('chaungjian_order')

    #获取生产按钮元素

    def get_shengchang_button(self):
        return self.f.get_element('shengchang')
    # 获取点选订单
    def get_click_dingdanbianhao(self):
        return self.f.get_element('click_dingdanbianhao')

    #获取选择供选择的订单按钮

    def get_select_dingdanbianhao(self):
        return self.f.get_element('select_dingdanbianhao')

    #获取上颌开始步文本框
    def get_up_start(self):
        return self.f.get_element('up_start')

    #获取上颌结束步文本框
    def get_up_end(self):
        return self.f.get_element('up_end')

    #获取下颌开始步文本框
    def get_lower_start(self):
        return self.f.get_element('lower_start')

    #获取下颌结束步文本框
    def get_lower_end(self):
        return self.f.get_element('lower_end')

    #获取确认下单按钮元素

    def get_queren_xiadan(self):
        return self.f.get_element('queren_xiadan')



