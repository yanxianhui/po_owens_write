from Page.erp_orderguanli_page import erp_orderguanli_page

class erp_orderguanli_handle():
    def __init__(self,driver):
        self.p=erp_orderguanli_page(driver)
    #点击订单管理设计按钮
    def click_ordergl_sheji_button(self):
        self.p.get_sheji_button().click()
    #点击订单管理创建订单按钮
    def click_ordergl_chaungjian_button(self):
        self.p.get_chaungjian_order_button().click()

    #订单管理点击生产按钮
    def click_shengchang_button(self):
        self.p.get_shengchang_button().click()

    #点击请选择订单编号
    def click_dingdanbianhao_button(self):
        self.p.get_click_dingdanbianhao().click()

    #选择订单编号
    def click_select_dingdanbianhao(self):
        self.p.get_select_dingdanbianhao().click()
    #输入上颌开始步数
    def send_up_start(self,aaa):
        self.p.get_up_start().send_keys(aaa)
    # 输入上颌结束步数
    def send_up_end(self,aaa):
        self.p.get_up_end().send_keys(aaa)
    # 输入下颌开始步数
    def send_lower_start(self,aaa):
        self.p.get_lower_start().send_keys(aaa)
    # 输入下颌结束步数
    def send_lower_end(self,aaa):
        self.p.get_lower_end().send_keys(aaa)

    #点击确认下单按钮
    def click_queren_xiadan_button(self):
        self.p.get_queren_xiadan().click()
